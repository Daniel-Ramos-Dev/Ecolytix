import json

from solana.rpc.api import Client

from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solders.instruction import Instruction
from solders.message import Message
from solders.transaction import Transaction

client = Client("https://api.devnet.solana.com")

MEMO_PROGRAM_ID = Pubkey.from_string(
    "MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr"
)

wallet = Keypair.from_json(
    open("/home/daniel/.config/solana/id.json").read()
)

def write_to_blockchain(data):

    memo = json.dumps(data)

    instruction = Instruction(
        MEMO_PROGRAM_ID,
        memo.encode(),
        []
    )

    latest_blockhash = client.get_latest_blockhash()

    message = Message.new_with_blockhash(
        [instruction],
        wallet.pubkey(),
        latest_blockhash.value.blockhash
    )

    tx = Transaction.new_unsigned(message)

    tx.sign([wallet], latest_blockhash.value.blockhash)

    response = client.send_transaction(tx)

    return str(response.value)