SEGMENT_BITS  = 4084
SEGMENT_BYTES = SEGMENT_BITS // 8  # 511

def iter_segments(raw: bytes):
    for i in range(0, len(raw), SEGMENT_BYTES):
        yield raw[i:i+SEGMENT_BYTES]
