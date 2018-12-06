import Web3 from 'web3'

let web3Instance = undefined;

if (typeof web3 !== 'undefined') {
  web3Instance = new Web3(web3.currentProvider);
} else {
  // Set the provider you want from Web3.providers
  web3Instance = new Web3(new Web3.providers.HttpProvider(process.env.web3ProviderUrl));
}

export default web3Instance
