from scapy.all import (
    Packet,
    BitField,
    StrLenField,
    bind_layers,
    TCP,
    UDP
)

class Port100Header(Packet):
    name = "Port100Header"
    fields_desc = [
        BitField("origin",          0, 4),   # 4 bits
        BitField("integrity_class", 0, 6),   # 6 bits
        BitField("assert_mode",     0, 4),   # 4 bits
        BitField("salt_window",     0, 12),  # 12 bits
        BitField("context_tag",     0, 8),   # 8 bits
        BitField("hash_stub",       0, 40),  # 40 bits
        # Remaining bytes are the 4084-bit segments (or multiple of them)
        StrLenField(
            "segments",
            default=b"",
            length_from=lambda pkt: pkt.underlayer.len - len(pkt)
            if hasattr(pkt.underlayer, "len") else None
        ),
    ]

# Bind to TCP/UDP port 100
bind_layers(TCP, Port100Header, dport=100)
bind_layers(TCP, Port100Header, sport=100)
bind_layers(UDP, Port100Header, dport=100)
bind_layers(UDP, Port100Header, sport=100)
