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

// It validates network and returns {'from': 'address'}
// from address it will make new transaction

promisify['transactionInfo'] = async function () {
  const networkId = await promisify['networkId']();
  if (String(process.env.web3NetworkId) != String(networkId)) {
    alert("process.env.web3NetworkId" + process.env.web3NetworkId)
    alert("networkId" + networkId)
    throw new Error("Wrong network id")
  }

  const accounts = await promisify['accounts']();
  if (accounts.length == 0) {
    throw new Error("Please install MetaMask or unlock it")
  }

  return {from: accounts[0]}
};

web3Instance.promisify = promisify;

export default web3Instance
