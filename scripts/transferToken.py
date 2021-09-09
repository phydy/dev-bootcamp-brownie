from brownie import ERC20Basic, config, accounts, network
 
def main():
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    erc20 = ERC20Basic[-1]
    transact = erc20.transfer(accounts[1], 200, {'from': account})
    transact.wait(1)
    print("Total Supply is", erc20.totalSupply())
