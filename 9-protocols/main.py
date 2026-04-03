import dis
import timeit
from msgpack_codec import MessagePackCodec
from bit_packer import BinaryStreamer

class ProtocolEngine:
    def __init__(self, db_name="storage.bin"):
        self.codec = MessagePackCodec()
        self.streamer = BinaryStreamer(db_name)

    def run_logic(self, record_id: int, metadata: dict):
        id_bytes = self.streamer.pack_fixed_data(record_id)
        payload_bytes = self.codec.encode(metadata)
        self.streamer.write_at(0, id_bytes + payload_bytes)

    def benchmark(self, data):
        t = timeit.timeit(lambda: self.run_logic(1, data), number=10000)
        avg_micro = (t / 10000) * 1_000_000
        print(f"Média: {avg_micro:.2f} µs")

    def inspect(self):
        dis.dis(self.run_logic)

if __name__ == "__main__":
    user_data = {"user": "dev_zero", "status": "active", "level": 99}
    engine = ProtocolEngine()
    engine.run_logic(101, user_data)
    engine.inspect()
    engine.benchmark(user_data)
