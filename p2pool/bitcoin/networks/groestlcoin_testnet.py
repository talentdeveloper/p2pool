import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '0b110907'.decode('hex')
P2P_PORT = 17777
ADDRESS_VERSION = 111
RPC_PORT = 17766
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'groestlcoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: __import__('groestlcoin_subsidy').getBlockBaseValue(0, height+1)
POW_FUNC = data.hash_groestl
BLOCK_PERIOD = 60 # s
SYMBOL = 'GRS'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Groestlcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Groestlcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.groestlcoin'), 'groestlcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs-test/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs-test/address.dws?'
TX_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs-test/tx.dws?'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**20 - 1)
DUMB_SCRYPT_DIFF = 2**12
DUST_THRESHOLD = 0.001e8
