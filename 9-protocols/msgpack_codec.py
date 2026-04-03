import msgpack 
import io 
import zlib
from typing import Any, Dict

class MessagePackCodec:
    def encode(self, data: Dict[str, Any]) -> bytes:
        packed = msgpack.packb(data)
        return zlib.compress(packed)
        
    def decode(self, bin_data: bytes) -> Dict[str, Any]:
        decompressed = zlib.decompress(bin_data)
        return msgpack.unpackb(decompressed)
