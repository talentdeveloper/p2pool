import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f9beb4d4'.decode('hex')
P2P_PORT = 1331
ADDRESS_VERSION = 36
RPC_PORT = 1441
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '00000ac5927c594d49cc0bdb81759d0da8297eb614683d3acb62f0703b639023')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: __import__('groestlcoin_subsidy').getBlockBaseValue(0, height+1)
POW_FUNC = data.hash_groestl
BLOCK_PERIOD = 60 # s
SYMBOL = 'GRS'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Groestlcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Groestlcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.groestlcoin'), 'groestlcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs/address.dws?'
TX_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs/tx.dws?'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**20 - 1)
DUMB_SCRYPT_DIFF = 2**12
DUST_THRESHOLD = 0.001e8
