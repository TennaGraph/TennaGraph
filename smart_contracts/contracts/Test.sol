pragma solidity ^0.4.0;

contract AssetsManager {

    enum Measuring {None, volume, weight, size, count, form}

    struct AssetType {
        uint id;
        bool isActive;
        string title;
        Measuring[] measures;
    }

    /**
    * @dev unique incremental id of AssetProperties
    */
    uint assetTypeNonce = 0;

    /**
    * @dev unique incremental id of AssetProperties
    */
    AssetType[] public availableAssetTypes;

    /**
    * @dev unique incremental id of asset
    */
    uint assetNonce = 0;

    /**
    * @dev an address of modified ERC721 smart contract
    */
    address public tokenContract;

    /**
    * @dev adds new asset type (materials, products and so on) to the system
    * @param _title title of asset type (water, steal, jam...)
    * @param _measures measures of this asset type (volume and weight...)
    */
    function addNewAssetType(string _title, Measuring[] _measures) public;

    /**
    * @dev suspends supporting the asset type with specified id
    * @param _id of asset type
    */
    function suspendAssetType(uint _id) public;


    function produceNewAsset(AssetType _assetType, bytes _args) public onlyProducer;

}
