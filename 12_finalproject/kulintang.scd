// Boot the server
(
  Server.default=s=Server.local;
  s.boot;
)

// Find path of kulintang samples
a = "/Users/Renzo Ledesma/mus305/renzol2/12_finalproject/samples/*.wav".pathMatch;

// Load samples into VKey
VKey(\kulintang).loadAsSeries(s, a, channels: 0);

// Get reference to database
k = VKey.db('kulintang');

// Play random gong
k.vkey(7.rand, 0, nil, 0.7);

// Setup callback to listen to OscMessages from musx
(
  o = OSCFunc({|msg, time, from, port|
	postln(msg.asString);
    // vkey args: keynum, start=0, dur=nil, amp=1, pan=0, out=0, ampenv=nil, bend=nil
	k.vkey(msg.at(1)-1, 0, nil, msg.at(4));
  }, '/musx/kulintang', nil, NetAddr.langPort);
);

// Stop server
s.quit();

s.scope;

