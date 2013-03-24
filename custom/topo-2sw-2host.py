"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's3' )
        downSwitch = self.addSwitch( 's4' )
	downHost = self.addHost( 'h5' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, downSwitch )
        self.addLink( downSwitch, downHost )
	self.addLink( leftSwitch, rightHost )
	self.addLink( downSwitch, rightHost )

topos = { 'mytopo': ( lambda: MyTopo() ) }
