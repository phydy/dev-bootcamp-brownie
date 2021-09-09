from brownie import ERC20Basic, config, accounts, network
from scripts.helpful_scripts import (
    get_account
)
 
def main():
    account = get_account() #accounts.add(config["wallets"]["from_key"]) or accounts[0]
    erc20 = ERC20Basic[-1]
    print("Total Supply is", erc20.totalSupply())
