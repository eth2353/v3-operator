from dataclasses import dataclass
from decimal import Decimal

from ens.constants import EMPTY_ADDR_HEX
from eth_typing import BlockNumber, ChecksumAddress, HexStr
from sw_utils.typings import Bytes32, ConsensusFork
from web3 import Web3
from web3.types import Wei

MAINNET = 'mainnet'
GOERLI = 'goerli'
GNOSIS = 'gnosis'
HOLESKY = 'holesky'

ETH_NETWORKS = [MAINNET, GOERLI, HOLESKY]
GNO_NETWORKS = [GNOSIS]


@dataclass
# pylint: disable-next=too-many-instance-attributes
class NetworkConfig:
    SYMBOL: str
    VALIDATORS_REGISTRY_CONTRACT_ADDRESS: ChecksumAddress  # consensus deposit contract
    VALIDATORS_REGISTRY_GENESIS_BLOCK: BlockNumber  # consensus deposit contract genesis
    KEEPER_CONTRACT_ADDRESS: ChecksumAddress
    KEEPER_GENESIS_BLOCK: BlockNumber
    V2_POOL_CONTRACT_ADDRESS: ChecksumAddress
    V2_POOL_GENESIS_BLOCK: BlockNumber
    V2_POOL_ESCROW_CONTRACT_ADDRESS: ChecksumAddress
    GENESIS_VAULT_CONTRACT_ADDRESS: ChecksumAddress
    GENESIS_VALIDATORS_ROOT: Bytes32
    GENESIS_VALIDATORS_IPFS_HASH: str
    SLOTS_PER_EPOCH: int
    SECONDS_PER_BLOCK: Decimal
    GENESIS_FORK_VERSION: bytes
    IS_POA: bool
    HOT_WALLET_MIN_BALANCE: Wei
    SHAPELLA_FORK_VERSION: bytes
    SHAPELLA_EPOCH: int
    MULTICALL_CONTRACT_ADDRESS: ChecksumAddress

    @property
    def SHAPELLA_FORK(self) -> ConsensusFork:
        return ConsensusFork(
            version=self.SHAPELLA_FORK_VERSION,
            epoch=self.SHAPELLA_EPOCH,
        )

    @property
    def IS_SUPPORT_V2_MIGRATION(self) -> bool:
        """Check if network support for v2-to-v3 protocol migration"""
        return Web3.to_checksum_address(EMPTY_ADDR_HEX) not in [
            self.V2_POOL_CONTRACT_ADDRESS,
            self.V2_POOL_ESCROW_CONTRACT_ADDRESS,
            self.GENESIS_VAULT_CONTRACT_ADDRESS,
        ]


NETWORKS = {
    MAINNET: NetworkConfig(
        SYMBOL='ETH',
        VALIDATORS_REGISTRY_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0x00000000219ab540356cBB839Cbe05303d7705Fa'
        ),
        VALIDATORS_REGISTRY_GENESIS_BLOCK=BlockNumber(11052983),
        KEEPER_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0x6B5815467da09DaA7DC83Db21c9239d98Bb487b5'
        ),
        KEEPER_GENESIS_BLOCK=BlockNumber(18470089),
        V2_POOL_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0xC874b064f465bdD6411D45734b56fac750Cda29A'
        ),
        V2_POOL_GENESIS_BLOCK=BlockNumber(11726297),
        V2_POOL_ESCROW_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0x2296e122c1a20Fca3CAc3371357BdAd3be0dF079'
        ),
        GENESIS_VAULT_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0xAC0F906E433d58FA868F936E8A43230473652885'
        ),
        GENESIS_VALIDATORS_ROOT=Bytes32(
            Web3.to_bytes(
                hexstr=HexStr('0x4b363db94e286120d76eb905340fdd4e54bfe9f06bf33ff6cf5ad27f511bfe95')
            )
        ),
        GENESIS_VALIDATORS_IPFS_HASH='bafybeidcgs5ijtdjm4y2m2p4oh6us3gcb7rjv4n75ub6ugv4tku44dgy3y',
        SLOTS_PER_EPOCH=32,
        SECONDS_PER_BLOCK=Decimal(12),
        GENESIS_FORK_VERSION=Web3.to_bytes(hexstr=HexStr('0x00000000')),
        IS_POA=False,
        HOT_WALLET_MIN_BALANCE=Web3.to_wei('0.03', 'ether'),
        SHAPELLA_FORK_VERSION=Web3.to_bytes(hexstr=HexStr('0x03000000')),
        SHAPELLA_EPOCH=194048,
        MULTICALL_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0xcA11bde05977b3631167028862bE2a173976CA11'
        ),
    ),
    HOLESKY: NetworkConfig(
        SYMBOL='HolETH',
        VALIDATORS_REGISTRY_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0x4242424242424242424242424242424242424242'
        ),
        VALIDATORS_REGISTRY_GENESIS_BLOCK=BlockNumber(0),
        KEEPER_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0xB580799Bf7d62721D1a523f0FDF2f5Ed7BA4e259'
        ),
        KEEPER_GENESIS_BLOCK=BlockNumber(215379),
        V2_POOL_CONTRACT_ADDRESS=Web3.to_checksum_address(EMPTY_ADDR_HEX),
        V2_POOL_GENESIS_BLOCK=BlockNumber(0),
        V2_POOL_ESCROW_CONTRACT_ADDRESS=Web3.to_checksum_address(EMPTY_ADDR_HEX),
        GENESIS_VAULT_CONTRACT_ADDRESS=Web3.to_checksum_address(EMPTY_ADDR_HEX),
        GENESIS_VALIDATORS_ROOT=Bytes32(
            Web3.to_bytes(
                hexstr=HexStr('0x9143aa7c615a7f7115e2b6aac319c03529df8242ae705fba9df39b79c59fa8b1')
            )
        ),
        GENESIS_VALIDATORS_IPFS_HASH='bafybeih2zhayrd6t5nnvzwmechcrxeejphr45lv4q7byxjqlapizghdtde',
        SLOTS_PER_EPOCH=32,
        SECONDS_PER_BLOCK=Decimal(12),
        GENESIS_FORK_VERSION=Web3.to_bytes(hexstr=HexStr('0x01017000')),
        IS_POA=False,
        HOT_WALLET_MIN_BALANCE=Web3.to_wei('0.03', 'ether'),
        SHAPELLA_FORK_VERSION=Web3.to_bytes(hexstr=HexStr('0x01017000')),
        SHAPELLA_EPOCH=256,
        MULTICALL_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0xcA11bde05977b3631167028862bE2a173976CA11'
        ),
    ),
    GOERLI: NetworkConfig(
        SYMBOL='GoerliETH',
        VALIDATORS_REGISTRY_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0xff50ed3d0ec03aC01D4C79aAd74928BFF48a7b2b'
        ),
        VALIDATORS_REGISTRY_GENESIS_BLOCK=BlockNumber(4367321),
        KEEPER_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0x893ceb1cF23475defE3747670EbE4b40e629c6fD'
        ),
        KEEPER_GENESIS_BLOCK=BlockNumber(9583358),
        V2_POOL_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0x8c1EfEcFb5c4F1099AB0460b5659342943764Df7'
        ),
        V2_POOL_GENESIS_BLOCK=BlockNumber(4468086),
        V2_POOL_ESCROW_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0x040F15C6b5Bfc5F324eCaB5864C38D4e1EEF4218'
        ),
        GENESIS_VAULT_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0x8B5c0d4c067Cf480766140B251B464de7F03B515'
        ),
        GENESIS_VALIDATORS_ROOT=Bytes32(
            Web3.to_bytes(
                hexstr=HexStr('0x043db0d9a83813551ee2f33450d23797757d430911a9320530ad8a0eabc43efb')
            )
        ),
        GENESIS_VALIDATORS_IPFS_HASH='QmQo3oLYxqWm75fbgJJkCaUttZoYVqZhZj9r99r1UsZVpu',
        SLOTS_PER_EPOCH=32,
        SECONDS_PER_BLOCK=Decimal(12),
        GENESIS_FORK_VERSION=Web3.to_bytes(hexstr=HexStr('0x00001020')),
        IS_POA=True,
        HOT_WALLET_MIN_BALANCE=Web3.to_wei('0.03', 'ether'),
        SHAPELLA_FORK_VERSION=Web3.to_bytes(hexstr=HexStr('0x03001020')),
        SHAPELLA_EPOCH=162304,
        MULTICALL_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0xcA11bde05977b3631167028862bE2a173976CA11'
        ),
    ),
    GNOSIS: NetworkConfig(
        SYMBOL='xDAI',
        VALIDATORS_REGISTRY_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0x0B98057eA310F4d31F2a452B414647007d1645d9'
        ),
        VALIDATORS_REGISTRY_GENESIS_BLOCK=BlockNumber(19469076),
        # TODO: replace with real values once contracts deployed
        KEEPER_CONTRACT_ADDRESS=Web3.to_checksum_address(EMPTY_ADDR_HEX),
        KEEPER_GENESIS_BLOCK=BlockNumber(0),
        V2_POOL_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0x2f99472b727e15EECf9B9eFF9F7481B85d3b4444'
        ),
        V2_POOL_GENESIS_BLOCK=BlockNumber(21275812),
        V2_POOL_ESCROW_CONTRACT_ADDRESS=Web3.to_checksum_address(EMPTY_ADDR_HEX),
        GENESIS_VAULT_CONTRACT_ADDRESS=Web3.to_checksum_address(EMPTY_ADDR_HEX),
        GENESIS_VALIDATORS_ROOT=Bytes32(
            Web3.to_bytes(
                hexstr=HexStr('0xf5dcb5564e829aab27264b9becd5dfaa017085611224cb3036f573368dbb9d47')
            )
        ),
        GENESIS_VALIDATORS_IPFS_HASH='',
        SLOTS_PER_EPOCH=32,
        SECONDS_PER_BLOCK=Decimal('6.8'),
        GENESIS_FORK_VERSION=Web3.to_bytes(hexstr=HexStr('0x00000064')),
        IS_POA=False,
        HOT_WALLET_MIN_BALANCE=Web3.to_wei('0.03', 'ether'),
        SHAPELLA_FORK_VERSION=Web3.to_bytes(hexstr=HexStr('0x0')),
        SHAPELLA_EPOCH=0,  # todo
        MULTICALL_CONTRACT_ADDRESS=Web3.to_checksum_address(
            '0xcA11bde05977b3631167028862bE2a173976CA11'
        ),
    ),
}
