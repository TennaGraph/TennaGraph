import Web3 from 'web3'

let web3Instance = undefined;

if (typeof web3 !== 'undefined') {
  web3Instance = new Web3(web3.currentProvider);
} else {
  // Set the provider you want from Web3.providers
  web3Instance = new Web3(new Web3.providers.HttpProvider(process.env.web3ProviderUrl));
}

const promisify = {}

promisify['networkId'] = function () {
  return new Promise(function (resolve, reject) {
    web3Instance.version.getNetwork((err, netId) => {
      if (netId) {
        resolve(netId)
      } else {
        reject(err)
      }
    })
  })
};

promisify['networkTitleForId'] = function (networkId) {
  return new Promise(function (resolve, reject) {
    switch (networkId) {
      case "1":
        resolve("Mainnet")
      case "2":
        resolve("Morden")
      case "3":
        resolve("Ropsten")
      case "4":
        resolve("Rinkeby")
      case "42":
        resolve("Kovan")
      default:
        reject("Unknown network id")
    }
  })
};

promisify['accounts'] = function () {
  return new Promise(function (resolve, reject) {
    web3Instance.eth.getAccounts((err, accounts) => {
      if (err) {
        reject(err)
      } else {
        resolve(accounts)
      }
    })
  })
};

promisify['checkNetwork'] = async function () {
  const networkId = await promisify['networkId']();
  const shouldBeNetworkId = String(process.env.web3NetworkId);
  if (shouldBeNetworkId != String(networkId)) {
    const networkTitle = await promisify['networkTitleForId'](shouldBeNetworkId);

    throw new Error("Wrong network. Please, open Metamask and choose " + networkTitle)
  }
};

// It validates network and returns {'from': 'address'}
// from address it will make new transaction

promisify['transactionInfo'] = async function () {
  await promisify['checkNetwork']();

  const accounts = await promisify['accounts']();
  if (accounts.length == 0) {
    throw new Error("Please install MetaMask or unlock it")
  }

  return {from: accounts[0]}
};

web3Instance.promisify = promisify;

export default web3Instance
