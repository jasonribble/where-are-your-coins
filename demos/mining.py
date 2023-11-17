#! /usr/bin/python
# Run me first!
import hashlib
import json
block_815149_hash = "000000000000000000040c606208a9c7f15ae0908dc6dddb9cd0ef6c0cf69681"

def proof_of_work(previous_block_hash, current_block_data):
    nonce = 0
    while True:
        data_string = f"{previous_block_hash}{json.dumps(current_block_data)}{nonce}"
        data_bytes = data_string.encode()

        hash_object = hashlib.sha256(data_bytes)
        hash_hex = hash_object.hexdigest()

        print(hash_hex)

        if hash_hex[:3] == "000":
            print(f"Nonce found: {nonce}")
            print(f"Hash: {hash_hex}")
            return nonce

        nonce += 1

# Previous block hash and current block data
previous_block_hash = block_815149_hash

next_block_data = {
    "id": "000000000000000000047a0baacb20399819c82d6983a545d849625c040380e5",
    "height": 815150,
    "version": 807436288,
    "timestamp": 1699036393,
    "tx_count": 4406,
    "size": 1637611,
    "weight": 3992929,
    "merkle_root": "812ed9e694255ccf724c0b06fadfc6f1d8fcc6dec49f44e417600b138affe70f",
    "bits": 386171284,
}

nonce = proof_of_work(previous_block_hash, next_block_data)

# The actual nonce of this block is 2166288761
