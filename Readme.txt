The purpose of this repository is to construct the MT80437 program. 
The MT80437 program is designed to work with other programs but it's main function is:
* To control the OSI-model from the data-link layer to storage media.
* To operate the QoS+ <writeoperation>
* To be a server and access point for java-based and memory-resident applications in a discrete physical network segment

The objective of this program is essentially to form a hash that is tied to a network segment, per user, per device, per second, and pass "pseudo-machine-access-control" messages in [datagram] and [frame] encapsulation for the "Port100" [Port100API(Port100(Program))].

This will occur in the following methods:

QoS+ message header proposal
---------------------------------
(QoS+)      |        QoS_D64 (bytecode)
---------------------------------

5               (0000)(0000)(0000)(0000)(0000)(0000)(0000)(0000)(0000)(0000)(0000)(0000)(0000)(0000)(0000)(0000)