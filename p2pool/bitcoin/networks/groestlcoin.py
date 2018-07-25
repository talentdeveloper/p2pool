import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f9beb4d4'.decode('hex')
P2P_PORT = 5332
ADDRESS_VERSION = 63 # must match to PUBKEY_ADDRESS
SEGWIT_ADDRESS_VERSION = 63 # must match to SCRIPT_ADDRESS
RPC_PORT = 5442
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, 'cb4df2fa9b4d6bc09d9502ed67f23397fcd4064512695c8a752f85d3f5f'))
            ))
SUBSIDY_FUNC = lambda height: __import__('groestlcoin_subsidy').getBlockBaseValue(0, height+1)
POW_FUNC = data.hash_groestl
BLOCK_PERIOD = 60 # s
SYMBOL = 'SFX'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Soferox') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Soferox/') if platform.system() == 'Darwin' else os.path.expanduser('~/.soferox'), 'soferox.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs/block.dws?'
ADDRESS_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs/address.dws?'
TX_EXPLORER_URL_PREFIX = 'http://chainz.cryptoid.info/grs/tx.dws?'
SANE_TARGET_RANGE= (2**256//1000000000000000000 - 1, 2**256//100000 - 1)
DUMB_SCRYPT_DIFF = 256
DUST_THRESHOLD = 0.001e8
HUMAN_READABLE_PART = 'sfx'
