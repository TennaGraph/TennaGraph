# Iconx Smart-Contracts Suite
ICONX Smart Contracts + Tests

To install all dependencies:
``` bash
npm install
```

To run tests:
``` bash
npm run test
```

To run code-coverage:
``` bash
npm run cov
```

ICONX Smart contracts are located at: contracts/Crowdsale/IconxCrowdsale.sol

This file consist of 3 main contracts:
- TokenContract (erc20 token)
- IconxTokensBank (contract which knows how much tokens users can withdraw after specific date)
- IconxCrowdsaleContract (crowdsale contract)

Other details are described inside each smart contract.