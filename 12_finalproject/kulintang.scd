Server.killAll
ServerOptions.outDevices

// Boot the server
(
s.options.outDevice = 'Audio Out';
s.waitForBoot({
	b = ();
	b.kulintang = PathName("samples/kulintang".resolveRelative).entries.collect({
	arg file;
	Buffer.readChannel(s, file.fullPath, channels:[0]);
});
	b.dabakan = PathName("samples/dabakan".resolveRelative).entries.collect({
		arg file;
		Buffer.readChannel(s, file.fullPath, channels:[0]);
	});
	b.babandir = PathName("samples/babandir".resolveRelative).entries.collect({
		arg file;
		Buffer.readChannel(s, file.fullPath, channels:[0]);
	});


});
)

(
// Define SynthDefs
SynthDef.new(\kulintang, {
	arg gongIndex, amp;

	var sig = Select.ar(gongIndex, [
		PlayBuf.ar(1, b.kulintang[0], doneAction: 2),
		PlayBuf.ar(1, b.kulintang[1], doneAction: 2),
		PlayBuf.ar(1, b.kulintang[2], doneAction: 2),
		PlayBuf.ar(1, b.kulintang[3], doneAction: 2),
		PlayBuf.ar(1, b.kulintang[4], doneAction: 2),
		PlayBuf.ar(1, b.kulintang[5], doneAction: 2),
		PlayBuf.ar(1, b.kulintang[6], doneAction: 2),
		PlayBuf.ar(1, b.kulintang[7], doneAction: 2),
	]);

	sig = BPF.ar(sig, 1000, 3.0);

	sig = sig * amp;
	Out.ar(0, sig);
}).add;

SynthDef.new(\dabakan, {
	arg index, amp;

	var sig = Select.ar(index, [
		PlayBuf.ar(1, b.dabakan[0], doneAction: 2),
		PlayBuf.ar(1, b.dabakan[1], doneAction: 2),
		PlayBuf.ar(1, b.dabakan[2], doneAction: 2),
		PlayBuf.ar(1, b.dabakan[3], doneAction: 2),
	]);

	sig = sig * amp;
	Out.ar(1, sig);
}).add;

SynthDef.new(\babandir, {
	arg index, amp;

	var sig = Select.ar(index, [
		PlayBuf.ar(1, b.babandir[0], doneAction: 2),
		PlayBuf.ar(1, b.babandir[1], doneAction: 2),
		PlayBuf.ar(1, b.babandir[2], doneAction: 2),
		PlayBuf.ar(1, b.babandir[3], doneAction: 2),
	]);

	sig = sig * amp;
	Out.ar(1, sig);
}).add;
)


// Setup callback to listen to OscMessages from musx
(
~prevGongIndex = -1;
~prevSynth = nil;
OSCdef.new(
	key: \kulintang,
	func: {
		|msg, time, from, port|
		var amp = msg[4] * exprand(0.2, 0.3);
		var gongIndex = msg[1] - 1;
		if (~prevGongIndex == gongIndex, {
			~prevSynth.free;
		});
		~prevSynth = Synth.new(\kulintang, [
			\gongIndex: gongIndex,
			\amp: amp,
		]);
		~prevGongIndex = gongIndex;
	},
	path: '/musx/kulintang',
	srcID: nil,
	recvPort: NetAddr.langPort
);

OSCdef.new(
	key: \dabakan,
	func: {
		|msg, time, from, port|
		var amp = msg[4] * exprand(0.2, 0.3);
		var index = msg[1] - 1;
		Synth.new(\dabakan, [
			\index: index,
			\amp: amp,
		]);
	},
	path: '/musx/dabakan',
	srcID: nil,
	recvPort: NetAddr.langPort
);

~prevBabandirIndex = -1;
~prevBabandirSynth = nil;
OSCdef.new(
	key: \babandir,
	func: {
		|msg, time, from, port|
		var amp = msg[4] * exprand(0.2, 0.3);
		var index = msg[1] - 1;
		if (~prevBabandirIndex == index, {
			~prevBabandirSynth.free;
		});
		~prevBabandirSynth = Synth.new(\babandir, [
			\index: index,
			\amp: amp,
		]);
		~prevBabandirIndex = index;
	},
	path: '/musx/babandir',
	srcID: nil,
	recvPort: NetAddr.langPort
);
)

// Show scope
s.scope;

// Stop server
s.quit();
