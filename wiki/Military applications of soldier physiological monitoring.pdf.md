# Military applications of soldier physiological monitoring.pdf

Source: junk_drawer/Military applications of soldier physiological monitoring.pdf

Category: [[other]]

## Summary
Journal of Science and Medicine in Sport 21 (2018) 1147–1153 Contents lists available at ScienceDirect Journal of Science and Medicine in Sport journal homepage: www.elsevier.com/locate/jsams Military applications of soldier physiological monitoring夽 Karl E. Friedl U.S. Army Research Institute of Environmental Medicine, USA

## Full Content
Journal of Science and Medicine in Sport 21 (2018) 1147–1153

Contents lists available at ScienceDirect

Journal of Science and Medicine in Sport
journal homepage: www.elsevier.com/locate/jsams

Military applications of soldier physiological monitoring夽
Karl E. Friedl
U.S. Army Research Institute of Environmental Medicine, USA

a r t i c l e

i n f o

Article history:
Received 12 September 2017
Received in revised form 10 March 2018
Accepted 11 June 2018
Available online 20 June 2018
Keywords:
Physiological models
Wearable sensors
Military performance
Thermal biology
Metabolic monitoring
Neurophysiology

a b s t r a c t
Wearable physiological status monitoring is part of modern precision medicine that permits predictions
about an individual’s health and performance from their real-time physiological status (RT-PSM) instead
of relying on population-based predictions informed by estimated human, mission, and environmental/ambient conditions. RT-PSM systems have useful military applications if they are soldier-acceptable
and provide important actionable information. Most commercially available systems do not address relevant military needs, typically lack the validated algorithms that make real time computed information
useful, and are not open architected to be integrated with the soldier technological ecology. Military RT-PSM development requires committed investments in iterative efforts involving physiologists,
biomedical engineers, and the soldier users. Military operational applications include: (1) technological enhancement of performance by providing individual status information to optimize self-regulation,
workload distribution, and enhanced team sensing/situational awareness; (2) detection of impending soldier failure from stress load (physical, psychological, and environmental); (3) earliest possible detection
of threat agent exposure that includes the “human sensor”; (4) casualty detection, triage, and early clinical
management; (5) optimization of individual health and ﬁtness readiness habits; and (6) long term health
risk-associated exposure monitoring and dosimetry. This paper is focused on the performance-related
applications and considers near term predictions such as thermal-work limits, alertness and ﬁtness for
duty status, musculoskeletal fatigue limits, neuropsychological status, and mission-speciﬁc physiological
status. Each new measurement capability has provided insights into soldier physiology and advances the
cycle of invention, lab and ﬁeld testing, new discovery and redesign.
Published by Elsevier Ltd on behalf of Sports Medicine Australia. This is an open access article under
the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

“Unless the void that exists between the scientist or engineer
and the war ﬁghter is recognized, a hiatus will exist between
the inventor who knows what they could invent, if they only
knew what was wanted, and the soldiers who know, or ought
to know, what they want and would ask for it if they only knew
how much science could do for them. You have never really
bridged that gap yet.”
Winston Churchill, World Crisis, v. 2, 19271
1. Introduction
Wearable physiological monitoring can provide predictions
about an individual’s health and performance from their realtime physiological state. This precision medicine approach offers
major improvements over population-based predictions derived

夽 Mandatory Disclaimer: The opinions and assertions in this paper are those of
the author and do not necessarily represent the ofﬁcial views or policies of the U.S.
Department of the Army
E-mail address: karl.e.friedl3.civ@mail.mil

from ambient conditions and the general context of a mission.
Advances in computing power and microelectronics make possible this improvement in human performance assessment, with real
time physiological measurement capabilities and data processing
that can provide actionable and important information about the
individual. This review summarizes current progress in the development of these systems for military applications.
Previously, predicting soldier work-rest cycles and training limits could only be addressed using generalized models based on
estimated inputs about individuals and ambient conditions.2 In this
example of thermal-workload limits, real time physiological status
monitoring (RT-PSM) now provides new military capability with
individual assessment of soldier performance limits.3,4 The technological advance has come about by turning the focus inward, to
consider the actual state of an individual, instead of extrapolating
from external conditions and assuming typical responses. Thermalwork strain monitoring is one of the ﬁrst military PSM applications
to be used outside of the research community but provides only
one example of near term uses (Table 1).
Currently available commercial systems generally do not satisfy the requirements for military use. Even when the systems offer

https://doi.org/10.1016/j.jsams.2018.06.004
1440-2440/Published by Elsevier Ltd on behalf of Sports Medicine Australia. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/
licenses/by-nc-nd/4.0/).

1148

K.E. Friedl / Journal of Science and Medicine in Sport 21 (2018) 1147–1153

Table 1
Some military applications of wearable physiological monitoring technologies.
Soldier performance and readiness applications (to be used by soldiers)
and leaders)
Speciﬁc outcome assessments in near term system development
• Thermal-work strain limits
• Alertness and ﬁtness for duty
• Impending musculoskeletal injury & physical fatigue limits
• Neuropsychological status (mood and cognitive status)
• Pulmonary exposures limiting performance
• Specialized environmental exposures (e.g., hypoxia, peripheral cold
monitoring)
Some likely use cases
• Training to personalized safe limits of performance
• Mission decision support tool (e.g., optimized route, pacing, soldier
status)
• Physiological controller for performance augmentation systems (e.g.,
agile microclimate cooling, exoskeleton activation/proprioception)
• Man-machine interface to distribute workload (i.e., stress management)
• Biofeedback to train self-regulated performance
• Situational awareness in networked squad (i.e., shared sensing)
• Materiel testing and acquisition/product selection decision tools
Health and medical management applications (to be used by medical)
providers)
• Casualty detection, remote triage, and medical management (e.g.,
hemorrhage)
• Chemical/biological threat agent exposure – early detection and
management
• Environmental/military occupational exposure dosimetry (e.g., blast
exposure)
• Health readiness behavioral management tool (e.g., Army Triad
initiative)

something more than raw physiological data, computed information such as recent sleep history or caloric expenditure, is usually
based on proprietary algorithms that cannot be properly reviewed
and validated, making the output unusable. Unsecure and powerdemanding Bluetooth connections and proprietary architectures
cannot be easily integrated into tactically secure systems and
military communications networks. The systems should not add
signiﬁcant weight to the soldier and they cannot require daily
recharge or battery replacement. Thus, reduced size, weight and
power (SWaP) is critical to soldier acceptability and tactical usability and relevant applications are best developed iteratively with the
intended users. These are some of the considerations to making a
RT-PSM system ﬁt into the technological ecosystem of the soldier
(Fig. 1).
The critical component of a RT-PSM system is the algorithm that
turns data into useful and actionable knowledge for a soldier or
a small unit leader. Useful information from a RT-PSM system is
deﬁned as vitally important alerts that can be acted on to affect
the outcome of a mission or, in a training environment, to improve
safety and effectiveness of the training. Physiological telemetry has
been an important research tool to investigate the full range of normal human responses outside of the laboratory; however, reams of
raw physiological data are not particularly useful in military applications. Even to a trained medic, a parameter such as elevated heart
rate could mean variously that an individual is: properly activated
for peak performance, hemorrhaging and needs urgent care, or
experiencing psychological distress. The validated algorithms that
turn data into useful information are fundamental to RT-PSM, and
these algorithms should then guide the minimal sensor set that is
required. A technology “push” from new and interesting sensors
must be at least matched by an informed “pull” strategy driven
by Army problems and leader information needs. This represents
the coordination gap that Churchill identiﬁed: “what the inventor
could invent” and “what the soldier wants”.1

2. Field measurement of energy metabolism and workload
demands
Energy expenditure is a metabolic parameter that is fundamental to many models and applications involving thermal, workload,
and injury risk predictions. For example, cold injury risks can be signiﬁcantly reduced during high energy expenditure with metabolic
heat production, while high physical activity levels are increasingly limited in hot environments. Activity energy expenditure
(AEE) has been used to assess workload; fatigue limits for commander foot march planning have been expressed in terms of
energy expenditure rates (although endurance time for operational missions and overuse injury risk in training would be more
practical translations of the workload information). Total daily
energy expenditure (TDEE) estimates are also used for ﬁtness and
weight management programs. Generalized predictions of AEE and
TDEE are not good enough. For example, population-based predictions of energy expenditure such as the original Goldman–Givoni
model and subsequent modiﬁcations provide general planning estimates for walking speed and load carriage but are inaccurate, with
underprediction of metabolic costs by as much as one third.5 The
recently reported Ludlow–Weyand model simpliﬁes assumptions
to walking speed, grade, and total mass and may prove to be more
generalizable, but this needs to be fully evaluated.6
Wearable systems have typically estimated individual TDEE
from heart rate or accelerometry.7,8 Triaxial accelerometry on the
trunk improves TDEE estimates over that predicted simply from
age, body mass, and height, with estimates within 1 MJ/d.9 The location of the sensors on the body is an important factor in capturing
the desired information. Wrist-worn heart rate measurements are
less reliable than chest or trunk, even after correction for motion
artifacts during intense exercise.10 If only one sensored site is
available, trunk is also more reliable than wrist for accelerometrybased TDEE.11 This is unfortunate as wear compliance is generally
better with a wrist-watch like system than other typical body
sites. Boot-worn systems can accurately estimation activity-based
energy expenditure (AEE) and classify types of activity.12 Simple
foot contact time from a boot-worn device provides AEE.13 Measures of foot contact time and heart rate over a period of time also
track changes in aerobic ﬁtness of an individual.14 Measuring distance traveled, including inertial navigation and global positioning
systems, combined with barometric measures to measure movement up and down, further increase opportunities to improve AEE
estimates.15
Monitoring workload associated with physical training injury
risk is an important target for wearable technologies as musculoskeletal injuries continue to be a major modiﬁable component
affecting military readiness.16 Energy expenditure is only one
component of these predictions. Patterns of movement and
ground reaction forces may predict impending injury, permitting
preventive “prehabilitation” such as gait retraining or other interventions. Sophisticated but intrusive wearable systems have been
used experimentally for ﬁeld biomechanical assessments. Simpler
“smart shoe” devices with sensors on each shoe have provided useful performance data based on pattern analyses.17 It has been rather
more difﬁcult to develop suitable footwear inserts to measure
ground reaction forces without causing foot irritation and without rapidly breaking down from use; a notable line of inquiry led
by Reed Hoyt has explored a succession of strategies ranging from
sensors in form-ﬁtted insoles to acoustic ground sensors to piezoelectric foam technologies. Development efforts in the Netherlands
and the U.S. have produced prototypes for ﬁeld studies on training
workload and load carriage.18,19 Parallel efforts have demonstrated
the feasibility of estimating ground reaction forces using only inertial sensors worn around each ankle, suggesting other options
outside the boot.20

K.E. Friedl / Journal of Science and Medicine in Sport 21 (2018) 1147–1153

1149

Fig. 1. The range of technical considerations for a real time physiological status monitoring system includes much more than the algorithms and physiological measurements
discussed in this paper. Close partnerships with the developer and user communities are necessary to the actual implementation of a soldier useable system.
Source: Reed Hoyt (USARIEM) and Jeffrey Palmer (MIT Lincoln Labs), unpublished.

More direct TDEE measurements may be obtainable with new
portable metabolic monitors that measure expired O2 and CO2 ,
represent technology advances that make century-old concepts
feasible.21,22 The advantage of more portable metabolic monitoring
systems is the access to more detailed aspects of energy metabolism
such as macronutrient nutrition. Knowledge about shifts between
lipid and carbohydrate metabolism provide insights about physiological posture in extreme conditions as well as more routine
uses such as progress in weight management.23 New technologies to measure water turnover/ﬂux will provide future sensing
of water balance related to performance for more precise and optimal hydration.24,25 Advances in metabolic monitoring are opening
the door to assessment of key circulating components of energy
metabolism such as glucose and lactate, associated with fatigue
limits affecting physical, cognitive, and behavioral performance.
Minimally invasive continuous glucose monitoring systems have
greatly improved individual management for diabetics; however,
these systems still require some form of analyte sampling through
the skin.26 Improved transcutaneous spectroscopic methods, sweat
sampling systems, and even breath analyses currently under investigation may soon reduce metabolic assessments to noninvasive
wear-and-forget systems.

3. A wearable monitoring application success:
thermal-work strain
In clinical medicine, hyperthermia is conﬁrmed by temperature
measurement in the context of an individual exhibiting neurological symptoms. But simply measuring core temperature to detect
hyperthermia without this context belies the physiological adaptation to persistence hunting. Humans are uniquely suited for
endurance running at high temperature, and core temperature
sustained at over 40 ◦ C for several hours in marathon runners is

associated with peak performance rather than indicating a medical
emergency (of course, soldiers have additional thermal and workload burdens, including personal protective equipment).27 Thus,
the core temperature monitoring with the ingestible temperature
pill has provided a useful ﬁeld research tool, but simple core temperature monitoring or prediction does not solve the problem of
detecting individuals approaching their limits of work in the heat.
Safe work limits have been addressed with thermal-work strain
(TWS) indices, using inputs such as core temperature combined
with heart rate,28 and several other developments have made this
a practical solution. One was the development of a core temperature predictive algorithm based on analysis of time series heart
rates to replace the need to swallow temperature pills.29 Another
was the development of a sufﬁciently accurate and reliable physiological measurement system. The U.S. Army invested heavily in
the testing, integration, and validation of monitoring technologies
which resulted in a commercially available chest worn system.4
Recent efforts have further reduced RT-PSM size, weight and power
requirements, improved comfort, and provide tactically acceptable
communications. A third aspect of improving practical but reliable
individual estimates of TWS limits has been the development of
an adaptive TWS index.3 The Army National Guard Bureau is an
early adopter of this enhanced capability, using RT-PSM technology to closely monitor limits of individuals performing critical tasks
while encapsulated in protective suits in specialized operations by
their Weapons of Mass Destruction Civil Support Teams (WMDCST).4 Personalized monitoring in hot training environments is also
being investigated, where it could improve training effectiveness
by permitting higher training workloads than might be predicted
by group-based predictive heat strain models.
Simple core temperature also does not provide actionable
information regarding hypothermia. Large drops in core temperatures have been observed without medical consequences in

1150

K.E. Friedl / Journal of Science and Medicine in Sport 21 (2018) 1147–1153

Ranger students and Marine Infantry school ofﬁcers during high
risk ﬁeld training, while hypothermia deaths have previously
occurred unexpectedly in moderate temperature conditions. Productive monitoring approaches will likely center on indicators of
thermoregulatory failure such as cessation of intense shivering
thermogenesis.30 This area of research is still immature although
the effects of cold on hands and feet is being intensively investigated with skin, boot, and glove temperature sensing to prevent
peripheral freezing cold injury and to sustain critical performance
capabilities, especially involving hands.31

sleep behaviors in soldiers, providing beneﬁt to health readiness
initiatives.42 Reliable measurement of sleep quality (e.g., sleep
stages) outside of a laboratory will be important to development
and evaluation of attempts to compress restorative sleep in the ﬁeld
for soldiers; feasibility of correctly measuring deep sleep and REM
sleep stages with a wrist-worn system has been demonstrated.43
More studies are also needed on the translation between the psychomotor vigilance task, the performance outcome measure often
used in sleep laboratories, and militarily-relevant performance
outcomes.44

4. Early models of alertness and ﬁtness for duty assessment
Situational awareness is a critical component of soldier readiness and this is an important target for alertness monitoring.
Sustained alertness applies to the point man on patrol, sentries, or
even military technicians monitoring computer displays. Even well
rested individuals concentrating on threat detection and friend–foe
identiﬁcation begin to increase errors after two hours of sustained
effort. Vehicle drivers face alertness challenges in tactical settings,
especially driving in low light conditions at night. Soldier effectiveness is reduced during night operations when performance
circadian rhythms are lowest and sleep drive is highest and attentional lapses and micro sleeps increase markedly with inadequate
sleep.
Early concepts for fatigue and acute alertness monitoring were
as simple as a mercury switch on the back of the helmet to
detect head bobbing. A more sensitive measure of attentional lapse
uses infrared reﬂectance to detect slow eyelid closure (PERCLOSE),
tracking retinas from a dashboard mounted system. This is more
reliable if built into a helmet or glasses that move with the head
to maintain alignment with the eyes. Eye movements (“oculometrics”) such as eye blinks, eye saccades, and pupillometry have long
attracted fatigue researchers as performance assessment predictors but are still only promising possibilities.32,33 Despite a large
Army investment in oculometrics evaluation systems intended for
assessment of ﬁtness for duty, the technology has not matured.
More complex EEG monitoring of alertness has been demonstrated
by computational neurophysiologists34 but has always been hampered by limitations on computing power and speed as well as
the intrusiveness of the EEG scalp electrodes. When power is not
a limiter, such as in a vehicle or aircraft, EEG monitoring of soldier
fatigue is feasible and has been used in performance research, but
a full array of scalp electrodes is overly intrusive for routine use.35
Simpler single channel EEG systems have been developed that
might eventually be positioned in a cap or in a helmet headband.36
The French military is now using a system developed by military
researchers to optimize rest and ﬂight schedules and to modify tactics, techniques and procedures for more effective performance.37
This represents an important near term military PSM application.
The value of near infrared spectroscopy forehead measurements,
perhaps in conjunction with single channel EEG, may add to alertness predictions.38
Measurement of sleep history has been used to predict alertness
status, especially when combined with the variation in alertness
expected through the circadian cycle in a two process sleep and
performance model.39 General conclusions can be drawn about
decreased performance and attention at various levels of sleep
restriction or hours of sleep deprivation but many moderating factors from genetics of sleep resilience to the effect of naps and
caffeine confound reliable performance predictions.40 Sleep history
is obtained from total sleep time estimated by triaxial accelerometry. The commonly used algorithms predict sleep duration with
>90% reliability but are poor at correctly classifying wake state
(∼60%).41 Nevertheless, sleep monitoring appears to help improve

5. Neurophysiological assessments of performance
readiness
Military leaders would like to have some assurance that individuals are competent to make critical decisions and to know if
someone is about to fail due to overwhelming psychological stress.
Early research efforts during the Korean War investigated predictive stress markers, and neuroendocrinologists further clariﬁed
stress mechanisms in combat studies during the Vietnam War.45
The markers that are useful in measuring acute stress, including appropriate stress responses to a novel threat, do not appear
to be useful predictors of imminent failure. Measureable physiological responses such as changes in skin conductance, heart rate
and heart rate variability, and components of voice are consistent
markers of acutely stressful events such as parachute training and
conﬁdence courses.45 Voice stress analysis detects an emotionally
stressful event and this response diminishes with increasing conﬁdence in subsequent trials, while elevated heart rate is a persistent
feature of appropriate stress activation in preparation for a dangerous task.45 Similarly, landing on a pitching aircraft carrier deck in a
storm at night provokes appropriate and measurable physiological
responses that are interesting in characterizing an emotionally signiﬁcant event and stress activation but do not provide actionable
information.45
New approaches from the growing ﬁeld of affective computing,
based on other aspects of voice and behavior, show predictive value
in important outcomes such as depression and cognitive impairment. A DARPA initiative, Detection and Computational Analysis
of Psychological Signals (DCAPS), was organized to target “honest signals” in human behavior that signal psychological status.
This led to advances in voice stress analysis, assessments of social
interactions through modern media, and the development of physiologically aware virtual agents (PAVA) such as the Institute of
Creative Technologies’ “SimSensei,” incorporating mental status
monitoring technologies such as eye gaze, body posture, voice
analysis, and even speech content analysis.46,47 Components of
speech have been further dissected by providing a differential
assessment of involved brain domains.48 Combined with facial unit
activation, voice analysis can successfully distinguished depressed
patients from nondepressed.49 Patterns of movement have been
used to detect changes in cognitive status. Meandering patterns of
movement, reﬂected in a high fractal “D” score, identify cognitive
impairment and separate demented from normal veterans.50 This
may also identify individuals with persistent symptoms following
traumatic brain injury.51 Combined with information from embedded neuropsychological testing, these technologies will provide
additional insights into neurocognitive status.52 In combination
with the thermal-work strain index, this neurocognitive assessment based on changes in movement patterns might provide
reliable prediction of both impending heat stroke and hypothermia. These neurophysiological efforts signiﬁcantly leverage current
research on wearable systems to improve the quality of life for
patients with chronic diseases such as Parkinson’s.53

K.E. Friedl / Journal of Science and Medicine in Sport 21 (2018) 1147–1153

Future monitoring will include other modes of sensing such as
volatile odor production. We know that humans produce unique
stress signals detectable by dogs, based on the emerging empirical value of diabetic alert dogs to Type 1 diabetics and psychiatric
dogs to veterans.54,55 At some point those distinguishing patterns of
movement, physiological response, or secretion of volatile organic
compounds may be useful in machine detection of what dogs
already can detect. Human odors are a potentially rich source of
information with speciﬁc volatile organic compounds produced
during infection and possibly following head injury, and new olfactory receptor-lined nanotube sensing technologies make detection
feasible.56,57
Moderating soldier “stress load” will be an important application of a neurophysiological monitoring capability. This application
is an essential component of future man-machine interfacing.
This was recognized in another DARPA research initiative on
“Augmented Cognition,” where redistribution of mental workload within teams, the amount and form of information displays,
and various types of performance augmentation were all based
on an assumption of a real time neurocognitive status monitoring capability.58 Another application is to detect and help reduce
maladaptive psychological stress responses in soldiers. Continued physiological activation in the hours following an intense
psychologically traumatic exposure has been postulated to contribute to later trauma disorders, and psychological ﬁrst aid
involving pharmacological interventions has been proposed. An
effective self-management calming alternative has been demonstrated using biofeedback from cardiovascular measures combined
with gaming technology on a smart phone.59

1151

protect against environmental threats to expeditionary suits for
astronauts would beneﬁt from RT-PSM metabolic sensing.
7. Practical considerations
Military leaders have well-founded concerns about adding more
information to an already overcrowded attentional space. Earlier
concepts of a “soldier dashboard” were derived from clinical practice where a patient’s vital signs are displayed with an impressive
range of data. The information needs of an intensive care unit specialist caring for a patient are not the same as the information needs
of a small unit leader orchestrating the performance of a team of soldiers. Equating soldiers to vehicles is even less appropriate. Humans
are not cars and a “dashboard” displaying human analogs of temperature, fuel, and maintenance requirements is a rather simplistic
view of useful monitoring for humans that can sense and communicate about their own systems. Leaders may actually want to
receive higher level computed information about things like gaps
in security due to real time attentional lapses of sentries; who is
about to fail due to cognitive or physical burdens that can be redistributed; or identify a soldier who should not be making critical
decisions because their head is not in the game (e.g., due to stress,
depression, or recent head impact). RT-PSM offers new capabilities
to leaders for alerts about soldier readiness status that they may
not otherwise readily detect, but these alerts must roll up into simple stoplight displays (i.e., red/yellow/green) that can be further
queried only if more information is required. Many applications of
RT-PSM may be reserved for training environments to better prepare for the operational environment, providing a technology assist
to teach individual and team performance limits and ensure safer
training.

6. Monitoring to overcome mission-speciﬁc physiological
limitations

8. Medical applications

Soldier performance may be enhanced by real time behavioral
guidance based on RT-PSM (“technological doping”). One of the
thematic session at the 4th International Congress on Soldier Physical Performance (ICSPP) provided examples of workload pacing
and accelerated acclimation that might be accomplished using PSM
tools.60 Many more such applications can be envisioned. For example, voluntary control of metabolic rate and heat production in
certain extreme conditions could provide soldiers with a performance and survival advantage. PSM-informed biofeedback might
provide soldiers with a capability that currently takes years of disciplined training, where Buddhist monks can increase and decrease
basal metabolism by 60% in either direction and increase ﬁnger and
toe temperatures.61,62 An increase or decrease of core body temperature by only 1 ◦ C is associated with a ∼15% change in metabolic
rate.
RT-PSM opens the door to many other solder performance
applications, including needs for specialized missions and environments. This calls for a plug-and-play design of the soldier system
so that it can be conﬁgured for speciﬁc mission needs, ranging from
respiratory monitoring in subterranean and dense urban environments to thermal threats from directed energy systems. Prediction
of hypoxic impairment of performance during ascent to altitude
is also tactically relevant, as many national borders and potential
sites of military conﬂict are formed by high terrestrial environments. Performance predictions based on RT-PSM monitoring of
cardiovascular parameters such as blood oxygen saturation can
guide staging to altitude and identify individual performance risk.
Military pilots are also at potential risk for “physiological events,”
unexplained episodes of hypoxia in the cockpit, that may compromise health and critical performance. Many closed environments,
including submarines and diving systems to vehicles sealed to

There are logical extensions of the current RT-PSM efforts that
serve the needs of medical specialists. This information is derived
from many of the same sensors already used for performance predictions and the same platform and data management architectures
would support these additional capabilities (Table 1). However,
these medical capabilities generally must follow behind the performance capabilities. The adoption of wearable systems only to
support remote medical triage, especially for live-dead detection,
has not garnered widespread interest from soldiers, even though
these were some of the ﬁrst capabilities developed by direction of
the Army medical department.63 Soldiers might be more agreeable
to wearing a performance-based RT-PSM that could also detect a
casualty event, support a “911” alert, and support medical management (Fig. 2).
Casualty detection, triage, and early clinical management would
likely involve many of the same physiological measures and primarily requires a set of “casualty algorithms” that detect and track
hemorrhage and other critical problems. Hemorrhage is the major
preventable cause of death on the battleﬁeld and systems to detect
hemorrhage and predict hemorrhage severity would be of immediate importance in conserving the ﬁghting strength.65 This might
be possible with algorithms that are currently in development,
such as the Compensatory Reserve Index (CRI) that quantiﬁes a
failing hemodynamic response due to intravascular volume depletion based on photoplethysmography (PPG) measurements.66 At
present, the medic brings a sophisticated suite of medical monitoring tools to the casualty and lacks the initial wounding detection
capability.67
Optimization of individual health and ﬁtness readiness habits
is already supported with commercially available ﬁtness systems
that serve as behavioral prompts as much as providing meaningful

1152

K.E. Friedl / Journal of Science and Medicine in Sport 21 (2018) 1147–1153

Fig. 2. Concepts for real time physiological status monitoring (RT-PSM) include a common sensors and communications architecture for a system that supports soldier
readiness status and performance, and will also be able to support medical needs.
Source: Friedl.64

data about total sleep time or daily activity in the U.S. Army Triad
Initiative.42 RT-PSM, combined with outward looking environmental sensors, may also become important for individual exposure
monitoring and dosimetry, tying deployment and occupational
exposures to longer term health risks (this may not require real
time information). At present, this involves extraordinarily complex issues of what to measure in the environment and in the
individual (e.g., acute responses, exposomic markers, etc.) and how
to relate these measurements to actual health outcomes. Recent
efforts with wearable blast sensors and mild traumatic brain injury
illustrate the practical challenges of linking measurable exposures
to health risks. Current work by programs exploring critical air
quality triggers and related respiratory distress signals in asthmatics may provide a new model approach to environmental exposure
and RT-PSM.68 Other RT-PSM efforts will also provide rapid warning of immediate risks from chemical and biological threat agents,
especially from inhalation threats. These other applications are
beyond the scope of this review but would likely build on the common PSM strategies and architecture.

9. Conclusions
Physiological sensors will have useful military applications
if they are soldier-acceptable and provide important actionable
information. This paper has focused on operational medicine priorities, considering the components of a “soldier readiness score”
comprised of thermal-work limits, alertness and ﬁtness for duty
status, musculoskeletal fatigue limits, neuropsychological status,
and mission-speciﬁc physiological status (e.g., hypoxia, pulmonary
threats, freezing cold). One of the most promising and still least
developed part of performance monitoring is to use measurements

of human physiological and behavioral signals to detect neurophysiological status, particularly in predicting individuals reaching
stress limits and with impending degraded performance.
Acknowledgements
This paper is dedicated to Frederick W. Hegge, PhD (1935–2000),
an Army neuropsychologist who led the Ofﬁce of Military Performance Assessment Technologies (OMPAT) in the 1980s and who
enabled and conﬁdently predicted the technological developments
for soldier physiological monitoring that exist today.
Most of the work presented in this paper is based on more
than two decades of USARIEM research that has been led by
Reed W. Hoyt. Concepts presented in this paper have also been
informed by discussions in meetings of the NATO Human Factors in Medicine (HFM) Research Technology Group (RTG) 260,
“Enhancing Warﬁghter Effectiveness with Wearable Bio-Sensors
and Physiological Models.” The many contributions to PSM development by Jeffrey Palmer and his bioengineering research team at
MIT Lincoln Laboratory are also gratefully acknowledged.
References
[1]. Churchill WS. The World Crisis: 1916–1918, 2. New York, Charles Scribner’s Sons,
1927. p. 564.
[2]. Potter AW, Blanchard LA, Friedl KE et al. Mathematical prediction of core body
temperature from environment, activity, and clothing: the heat strain decision
aid (HSDA). J Therm Biol 2017; 64:78–85.
[3]. Buller MJ, Welles AP, Friedl KE. Wearable physiological monitoring for human
thermal-work strain optimization. J Appl Physiol 2018; 124(2):432–441.
[4]. Tharion WJ, Friedl KE, Buller MJ et al. Evolution of physiological status monitoring for ambulatory military applications, in The Cognitive and Behavioral
Neuroscience of Human Performance in Extreme Settings, Matthews Michael D,
Schnyer David, editors, New York, NY, Oxford University Press, 2019, (in press).

K.E. Friedl / Journal of Science and Medicine in Sport 21 (2018) 1147–1153
[5]. Drain JR, Aisbett B, Lewis M, Billing DC. The Pandolf equation under-predicts
the metabolic rate of contemporary military load carriage. J Sci Med Sport 2017;
20:S104–S108.
[6]. Ludlow LW, Weyand PG. Walking economy is predictably determined by speed:
grade and gravitational load. J Appl Physiol 2017; 123(5):1288–1302.
[7]. Freedson PS, Miller K. Objective monitoring of physical activity using motion
sensors and heart rate. Res Quart Exerc Sport 2000; 71(Suppl. 2):21–29.
[8]. Spurr GB, Prentice AM, Murgatroyd PR et al. Energy expenditure from minuteby-minute heart-rate recording: comparison with indirect calorimetry. Amer J
Clin Nutr 1988; 48(3):552–559.
[9]. Plasqui G, Joosen AM, Kester AD et al. Measuring free-living energy expenditure and physical activity with triaxial accelerometry. Obesity 2005;
13(8):1363–1369.
[10]. Zong C, Jafari R. Robust heart rate estimation using wrist-based PPG signals
in the presence of intense physical activities. In: Engineering in Medicine and
Biology Society (EMBC), 2015 37th Annual International Conference of the IEEE
2015: 8078–8082.
[11]. Chen KY, Acra SA, Majchrzak K et al. Predicting energy expenditure of physical activity using hip-and wrist-worn accelerometers. Diab Technol Therapeutics
2003; 5(6):1023–1033.
[12]. Hoyt RW, Buller MJ, Santee WR et al. Total energy expenditure estimated using
foot–ground contact pedometry. Diab Technol Therapeutics 2004; 6(1):71–81.
[13]. Hoyt RW, Knapik JJ, Lanza JF et al. Ambulatory foot contact monitor to estimate
metabolic cost of human locomotion. J Appl Physiol 1994; 76(4):1818–1822.
[14]. Weyand PG, Kelly M, Blackadar T et al. Ambulatory estimates of maximal aerobic
power from foot-ground contact times and heart rates in running humans. J Appl
Physiol 2001; 91(1):451–458.
[15]. Strozzi N, Parisi F, Ferrari G. A multiﬂoor hybrid inertial/barometric navigation
system, 2016 International Conference on Indoor Positioning and Indoor Navigation
(IPIN), 2018, p. 1–5.
[16]. Hauret KG, Jones BH, Bullock SH et al. Musculoskeletal injuries: description of
an under-recognized injury problem among military personnel. Amer J Prev Med
2010; 38(1):S61–S70.
[17]. Eskoﬁer B, Hoenig F, Kuehner P. Classiﬁcation of perceived running fatigue in
digital sports, 2008 International Conference on Pattern Recognition, 2018, p. 1–4.
[18]. Lacirignola J, Weston C, Byrd K et al. Instrumented footwear inserts: a new tool
for measuring forces and biomechanical state changes during dynamic movements, 2017 IEEE 14th International Conference on Wearable and Implantable Body
Sensor Networks (BSN) 2017, 2017, p. 119–124.
[19]. Valk PJ, Veenstra BJ. Military Performance and Health Monitoring in Extreme
environments. Technical Report, Netherlands, TNO Defence Security and Safety,
Soesterberg, 2009.
[20]. Clark KP, Ryan LJ, Weyand PG. A general relationship links gait mechanics and
running ground reaction forces. J Exper Biol 2017; 220(2):247–258.
[21]. Candell LM, Ferraiolo C, Shaw GA, et al., inventors. Systems, apparatus, and methods related to modeling, monitoring, and/or managing metabolism. United States
patent application US 15/221,313. 2016 Jul 27.
[22]. Committee on Metabolic Monitoring for Military Field Applications. Institute of
Medicine. Monitoring Metabolic Status: Predicting Decrements in Physiological and
Cognitive Performance, Washington D.C, National Academies Press, 2004.
[23]. Gribok A, Leger JL, Stevens M et al. Measuring the short-term substrate utilization response to high-carbohydrate and high-fat meals in the whole-body
indirect calorimeter. Physiol Report 2016; 4(12):e12835.
[24]. Nolte H, Noakes TD, Van Vuuren B. Ad libitum ﬂuid replacement in military personnel during a 4-h route march. Med Sci Sports Exerc 2010; 42(9):1675–1680.
[25]. First International Workshop on Hydration Monitoring Technologies. 2017 IEEE
14th International Conference on Wearable and Implantable Body Sensor Networks
(BSN), Eindhoven, Netherlands. May 12, 2017.
[26]. Klonoff DC. Continuous glucose monitoring. Diab Care 2005; 28(5):1231–1239.
[27]. Maron MB, Wagner JA, Horvath SM. Thermoregulatory responses during competitive marathon running. J Appl Physiol 1977; 42(6):909–914.
[28]. Moran DS, Shitzer A, Pandolf KB. A physiological strain index to evaluate heat
stress. Amer J Physiol 1998; 275(1):R129–34.
[29]. Buller MJ, Tharion WJ, Cheuvront SN et al. Estimation of human core temperature
from sequential heart rate observations. Physiol Meas 2013; 34(7):781.
[30]. Young AJ, Castellani JW, O’Brien C et al. Exertional fatigue, sleep loss, and negative energy balance increase susceptibility to hypothermia. J Appl Physiol 1998;
85(4):1210–1217.
[31]. Xu X, Santee WR, Gonzalez RR, et al. Prediction of hand manual performance during
cold exposure. SAE Technical Paper 2004-01-2348, 2004 (available at: https://doi.
org/10.4271/2004-01-2348, Last Accessed 4 March 2018).
[32]. Brozek J. Quantitative criteria of oculomotor performance and fatigue. J Appl
Physiol 1949; 2(5):247–260.
[33]. Van Orden KF, Jung TP, Makeig S. Combined eye activity measures accurately
estimate changes in sustained visual task performance. Biol Psychol 2000;
52(3):221–240.
[34]. Jung TP, Makeig S, Stensmo M et al. Estimating alertness from the EEG power
spectrum. IEEE Trans Biomed Engineering 1997; 44(1):60–69.
[35]. Caldwell JA, Hall KK, Erickson BS. EEG data collected from helicopter pilots in
ﬂight are sufﬁciently sensitive to detect increased fatigue from sleep deprivation. Int J Aviat Psychol 2002; 12(1):19–32.
[36]. Sauvet F, Bougard C, Coroenne M et al. In-ﬂight automatic detection of vigilance states using a single EEG channel. IEEE Trans Biomed Engineering 2014;
61(12):2840–2847.
[37]. Chennaoui M, Van Beers P, Caid S et al. Microsleep and alertness monitoring in
French Air Force long haul pilots. J Sci Med Sport 2017; 20:S134.

1153

[38]. Strangman GE, Ivkovic V, Zhang Q. Wearable brain imaging with multi-modal
physiological recording. J Appl Physiol 2018; 124(3):564–572.
[39]. Redmond DP, Hegge FW. Observations on the design and speciﬁcation of
a wrist-worn human activity monitoring system. Behav Res Methods 1985;
17(6):659–669.
[40]. Van Dongen H. Comparison of mathematical model predictions to experimental
data of fatigue and performance. Aviat Space Environ Med 2004; 75(3):A15–A36.
[41]. Rupp TL, Balkin TJ. Comparison of motionlogger watch and actiwatch actigraphs
to polysomnography for sleep/wake estimation in healthy young adults. Behav
Res Methods 2011; 43(4):1152–1160.
[42]. Adler AB, Gunia BC, Bliese PD et al. Using actigraphy feedback to improve sleep in
soldiers: an exploratory trial. Sleep Health: J Nat Sleep Found 2017; 3(2):126–131.
[43]. Mantua J, Gravel N, Spencer R. Reliability of sleep measures from four personal health monitoring devices compared to research-based actigraphy and
polysomnography. Sensors 2016; 16(5):646.
[44]. Lieberman HR, Falco CM, Slade SS. Carbohydrate administration during a day of
sustained aerobic activity improves vigilance, as assessed by a novel ambulatory
monitoring device, and mood. Amer J Clin Nutr 2002; 76(1):120–127.
[45]. Friedl KE, Grate SJ. Metabolic enhancement of the soldier brain, in The Cognitive
and Behavioral Neuroscience of Human Performance in Extreme Settings, Matthews
Michael D, Schnyer David, editors, New York NY, Oxford University Press, 2019,
(in press).
[46]. DeVault D, Artstein R, Benn G et al. SimSensei Kiosk: a virtual human interviewer
for healthcare decision support, Proceedings of the 2014 international conference
on Autonomous agents and multi-agent systems, 2014, p. 1061–1068.
[47]. Scherer S, Stratou G, Gratch J, Morency LP. Investigating voice quality as a
speaker-independent indicator of depression and PTSD. In: Interspeech 2013,
pp. 847-851.
[48]. Cummins N, Scherer S, Krajewski J et al. A review of depression and suicide risk
assessment using speech analysis. Speech Comm 2015; 71:10–49.
[49]. Williamson JR, Quatieri TF, Helfer BS et al. Vocal biomarkers of depression based
on motor incoordination, Proc 3rd ACM Int Workshop on Audio/Visual Emotion
Challenge, 2013, p. 41–48.
[50]. Kearns WD, Fozard JL, Nams VO. Movement path tortuosity in free ambulation: relationships to age and brain disease. IEEE J Biomed Health Inform 2017;
21(2):539–548.
[51]. Kearns WD, Scott S, Fozard JL et al. Decreased movement path tortuosity is associated with improved functional status in patients with traumatic brain injury.
J Head Trauma Rehab 2016; 31(1):E13–E19.
[52]. Friedl KE, Grate SJ, Proctor SP et al. Army research needs for automated neuropsychological tests: monitoring soldier health and performance status. Arch
Clin Neuropsychol 2007; 22:7–14.
[53]. Stamford JA, Schmidt PN, Friedl KE. What engineering technology could do for
quality of life in Parkinson’s disease: a review of current needs and opportunities.
IEEE J Biomed Health Inform 2015; 19(6):1862–1872.
[54]. Rooney NJ, Morant S, Guest C. Investigation into the value of trained glycaemia
alert dogs to clients with type I diabetes. PloS One 2013; 8(8):e69921.
[55]. Pleil J, Giese R. Integrating exhaled breath diagnostics by disease-snifﬁng dogs
with instrumental laboratory analysis. J Breath Res 2017; 11(3):032001.
[56]. Goldsmith BR, Mitala Jr JJ, Josue J et al. Biomimetic chemical sensors
using nanoelectronic readout of olfactory receptor proteins. ACS Nano 2011;
5(7):5408–5416.
[57]. Sethi S, Nanda R, Chakraborty T. Clinical application of volatile organic compound analysis for detecting infectious diseases. Clin Microbiol Rev 2013;
26(3):462–475.
[58]. Stanney KM, Schmorrow DD, Johnston M et al. Augmented cognition: an
overview. Rev Hum Factors Ergonomics 2009; 5(1):195–224.
[59]. Russoniello CV, O’Brien K, Parks JM. The effectiveness of casual video games in
improving mood and decreasing stress. J Cyber Ther Rehab 2009; 2(1):53–66.
[60]. Friedl K, Buller M. Session 14: non-pharmacological military performance
enhancement technologies. J Sci Med Sport 2017 2017; 20:S93–S95.
[61]. Benson H, Malhotra MS, Goldman RF et al. Three case reports of the metabolic
and electroencephalographic changes during advanced Buddhist meditation
techniques. Behav Med 1990; 16(2):90–95.
[62]. Benson H, Lehmann JW, Malhotraf MS et al. Body temperature changes during
the practice of g Tum-mo yoga. Nature 1982; 295:21–22.
[63]. Savell CT, Borsotto M, Reifman J, Hoyt RW. Life sign decision support algorithms.
InMedinfo 2004; 145:1453–1457.
[64]. Friedl KE. Is it possible to monitor the warﬁghter for prediction of performance
deterioration? Pp. 7.1-7.10, In: Workshop on operational fatigue. Technical Report
RTO-HFM/WS-151. Research and Technological Organization, North Atlantic
Treaty Organization, Neuilly-sur-Seine Cedex, France. 2008.
[65]. Eastridge BJ, Mabry RL, Seguin P et al. Death on the battleﬁeld (2001-2011):
implications for the future of combat casualty care. J Trauma Acute Care Surg
2012; 73(6):S431–S437.
[66]. Johnson M, Alarhayem A, Convertino V et al. Compensatory reserve Index: performance of a novel monitoring technology to identify the bleeding trauma
patient. Shock 2018; 49(3):295–300.
[67]. Moulton SL, Mulligan J, Santoro MA et al. Validation of a noninvasive monitor
to continuously trend individual responses to hypovolemia. J Trauma Acute Care
Surg 2017; 83(1):S104–S111.
[68]. Misra V, Lee B, Manickam P et al. Ultra-low power sensing platform for personal
health and personal environmental monitoring, Electron Devices Meeting (IEDM),
2015 IEEE International 2015, 2018,. pp. 13-1.



## Metadata
- Source file: junk_drawer/Military applications of soldier physiological monitoring.pdf
- Extracted: 2026-05-18
- Category: other
