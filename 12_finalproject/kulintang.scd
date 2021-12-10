// Boot the server
(
  Server.default=s=Server.local;
  s.boot;
)

// Find path of kulintang samples
a = "/Users/Renzo Ledesma/mus305/renzol2/12_finalproject/samples/kulintang*.wav".pathMatch;

// Find path of dabakan samples
b = "/Users/Renzo Ledesma/mus305/renzol2/12_finalproject/samples/dabakan*.wav".pathMatch;

// Load samples into VKey
VKey(\kulintang).loadAsSeries(s, a, channels: 0);
VKey(\dabakan).loadAsSeries(s, b, channels: 0);

// Get reference to database
k = VKey.db('kulintang');
d = VKey.db('dabakan');

// Play random note
k.vkey(7.rand, 0, nil, 0.7);
d.vkey(7.rand, 0, nil, 0.7);

// Setup callback to listen to OscMessages from musx
(
  o = OSCFunc({|msg, time, from, port|
	// postln(msg.asString);
    // vkey args: keynum, start=0, dur=nil, amp=1, pan=0, out=0, ampenv=nil, bend=nil
	k.vkey(msg.at(1)-1, 0, nil, msg.at(4));
  }, '/musx/kulintang', nil, NetAddr.langPort);
);

(
  p = OSCFunc({|msg, time, from, port|
	// postln(msg.asString);
    // vkey args: keynum, start=0, dur=nil, amp=1, pan=0, out=0, ampenv=nil, bend=nil
	d.vkey(msg.at(1)-1, 0, nil, msg.at(4));
  }, '/musx/dabakan', nil, NetAddr.langPort);
);

// Show scope
s.scope;

// Stop server
s.quit();

s.scope;

