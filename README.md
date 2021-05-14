# chord-check
What is it?
    It is a neural network--and supporting scripts--that identifies chords.

How does this work?
    The chord class generates waveforms that match the expected waveforms of 
    musical chords. These chords have randomly selected types, keys, and inversion.
    These generated waveforms are then used to train the neural net.

Status:
    The neural net is in a state where training is possible. However, when the training 
    process began, it became evident that the computational power available to my 
    personal computer where not suffucient to train on any practical time scale.
    I plan to find a way to access more computing power. I also plan to incorporate
    this network into a service where users can insert a song and get its chords.
