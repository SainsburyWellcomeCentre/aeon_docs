(target-about)=
# About

The brain's computations are shaped by evolutionary pressures related to survival and the resulting behavioural responses. 
Understanding the neural basis of natural behaviours is crucial for advancing our knowledge of the brain, as it sheds light on the functions of neural circuits in processing real-world stimuli. 
However, replicating natural conditions in a laboratory setting presents a challenge, as it requires simulating complex and dynamic environments which include the presence of conspecifics. 
It also requires monitoring over extended periods of time, all while allowing parametric control over key experimental variables and rigorous measurement of behaviour and neural activity.

Aeon is an open-source platform designed to study the neural basis of ethological behaviours over naturalistic timescales, ranging from weeks to months.
At its core, the setup is a modular, scalable, and programmable arena in which animals live. 
The arena can be equipped with various combinations of [interactive and non-interactive modules](target-hardware),
including, but not limited to, feeders, nesting areas, microphones, RFID readers, magnetic encoders, weighing scales, and high-speed cameras. 
This allows mimicking of complex and dynamic environments, thereby enabling animals to exhibit different natural behaviours, 
such as foraging, nesting, escape and social interaction. 
The large array of sensors in the arena additionally allows for continuous tracking of animal position, pose and identity, which in turn enables
multidimensional quantification of behavioural dynamics and internal states at millisecond resolution.

For an in-depth look at the unique challenges and opportunities presented by the datasets collected in Aeon, please refer to our [Design Considerations](target-design-considerations).
If you have any questions or need further information, feel free to reach out to the [project maintainers](target-project-maintainers).

(target-project-maintainers)=
## Project Maintainers

* Jai Bhagat (jai.bhagat.21@ucl.ac.uk)
* Gonçalo Lopes (g.lopes@neurogears.org)
* Dario Campagner (d.campagner@ucl.ac.uk)
* Chang Huan Lo (changhuan.lo@ucl.ac.uk)

(target-project-contributors)=
## Contributors
Dario Campagner[^1][^2], Jai Bhagat[^1], Gonçalo Lopes[^3], Lorenza Calcaterra[^1], 
Jaerong Ahn[^4], André Almeida[^3], Filipe Carvalho[^3], Bruno Cruz[^3], 
Andrew Erskine[^3], Orsolya Folsz[^1], Zimo Li[^2], Chang Huan Lo[^1], 
Thinh Nguyen[^4], Anaya Pouget[^1], Joaquin Rapela[^2], Jasmine Reggiani[^1], 
Thomas Ryan[^3], The SWC foraging behaviour working group[^1][^2]

[^1]: Sainsbury Wellcome Centre, UCL
[^2]: Gatsby CNU, UCL
[^3]: NeuroGEARS Ltd, London
[^4]: DataJoint Neuro, Vathes LLC, Houston, TX

## Code of Conduct

Aeon is dedicated to providing a welcoming and positive experience for all its participants. We encourage respectful and considerate behavior, and we expect our community members to adhere to these principles. Please read our [Code of Conduct](target-code-of-conduct) for more details on our community guidelines and expectations.

:::{toctree}
:maxdepth: 1
:hidden:

design_considerations
code_of_conduct
license