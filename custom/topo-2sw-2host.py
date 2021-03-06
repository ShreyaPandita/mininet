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
	downHost1 = self.addHost( 'h5' )
	downHost2 = self.addHost( 'h6' )
	downHost3 = self.addHost( 'h7' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, downSwitch )
        self.addLink( downSwitch, downHost1 )
	self.addLink( leftSwitch, rightHost )
	self.addLink( downSwitch, rightHost )
	self.addLink( downHost2, downSwitch )
	self.addLink( leftSwitch, downHost3 )
	
topos = { 'mytopo': ( lambda: MyTopo() ) }
