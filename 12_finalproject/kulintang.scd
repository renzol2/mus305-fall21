// Boot the server
(
  Server.default=s=Server.local;
  s.boot;
)


// Find path of kulintang samples
x = "/Users/Renzo Ledesma/mus305/renzol2/12_finalproject/samples/kulintang/*.wav".pathMatch;

// Find path of dabakan samples
y = "/Users/Renzo Ledesma/mus305/renzol2/12_finalproject/samples/dabakan/*.wav".pathMatch;

// Find path of babandir samples
z = "/Users/Renzo Ledesma/mus305/renzol2/12_finalproject/samples/babandir/*.wav".pathMatch;

// Load samples into VKey
(
VKey(\kulintang).loadAsSeries(s, x, channels: 0);
VKey(\dabakan).loadAsSeries(s, y, channels: 0);
VKey(\babandir).loadAsSeries(s, z, channels: 0);
)

// Get reference to database
k = VKey.db('kulintang');
d = VKey.db('dabakan');
b = VKey.db('babandir');

// Play random note
k.vkey(7.rand, 0, nil, 0.7);
d.vkey(7.rand, 0, nil, 0.7);
b.vkey(4.rand, 0, nil, 0.7);

// Setup callback to listen to OscMessages from musx
(
  o = OSCFunc({|msg, time, from, port|
	k.vkey(msg.at(1)-1, 0, nil, msg.at(4));
  }, '/musx/kulintang', nil, NetAddr.langPort);
);

(
  p = OSCFunc({|msg, time, from, port|
	d.vkey(msg.at(1)-1, 0, nil, msg.at(4));
  }, '/musx/dabakan', nil, NetAddr.langPort);
);

(
  q = OSCFunc({|msg, time, from, port|
	b.vkey((msg.at(1)-1) % 4, 0, nil, msg.at(4));
  }, '/musx/babandir', nil, NetAddr.langPort);
);

// Show scope
s.scope;

// Stop server
s.quit();
