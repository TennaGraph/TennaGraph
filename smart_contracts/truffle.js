require('babel-register');
require("babel-register")({
    ignore: /node_modules(?!\/zeppelin-solidity)/,
    presets: [
        ["env", {
            "targets": {
                "node": "8.0"
            }
        }]
    ],
    retainLines: true,
});
require('babel-polyfill');

module.exports = {
    // See <http://truffleframework.com/docs/advanced/configuration>
    // to customize your Truffle configuration!
    networks: {
        development: {
            host: 'localhost',
            port: 8544,
            gas: 100000000,
            network_id: '*', // eslint-disable-line camelcase
        },
        coverage: {
            host: 'localhost',
            network_id: '*', // eslint-disable-line camelcase
            port: 8555,
            gas: 0xfffffffffff,
            gasPrice: 0x01,
        },
        testrpc: {
            host: 'localhost',
            port: 8544,
            network_id: '*', // eslint-disable-line camelcase
        },
        ganache: {
            host: 'localhost',
            port: 7545,
            network_id: '*', // eslint-disable-line camelcase
        },
    },
};