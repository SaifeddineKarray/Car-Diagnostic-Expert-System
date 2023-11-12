from experta import *


class CarDiagnostic(KnowledgeEngine):
    def __init__(self,input):
        super().__init__()

        self.problem_symptoms = {
            "Faulty Spark Plugs": {"engine_start", "fuel_economy"},
            "Clogged Air Filter": {"fuel_economy"},
            "Leaking Head Gasket": {"engine_start", "overheating", "excessive_exhaust_smoke"},
            "Faulty Radiator": {"overheating"},
            "Malfunctioning Oxygen Sensor": {"engine_start", "fuel_economy", "excessive_exhaust_smoke"},
            "Worn Brake Pads": {"poor_braking"},
            "Damaged Suspension Bushings": {"unusual_noise"},
            "Unbalanced Tires/Wheels": {"unusual_noise", "poor_braking"},
            "Worn Out Clutch": {"engine_start", "unusual_noise", "car_vibrates"},
            "Faulty Fuel Pump": {"fuel_economy", "car_vibrates"},
            "Faulty Ignition Coil": {"engine_start", "fuel_economy"}
        }

        self.input=input

    def find_closest_problem(self, symptoms):
        max_similarity = -1
        closest_problem = None

        for problem, problem_symptoms in self.problem_symptoms.items():
            similarity = len(symptoms & problem_symptoms) / \
                len(symptoms | problem_symptoms)
            if similarity > max_similarity:
                max_similarity = similarity
                closest_problem = problem

        return closest_problem

    def declare_symptom(self, symptom_name, question):
        user_input = input(question)
        fact_dict = {symptom_name: user_input}
        self.declare(Fact(**fact_dict))

    @DefFacts()
    def _initial_action(self):
        yield Fact(action="find_issue")
        # adding facts from the interface
        yield Fact(engine_start=self.input[0])
        yield Fact(fuel_economy=self.input[1])
        yield Fact(overheating=self.input[2])
        yield Fact(excessive_exhaust_smoke=self.input[3])
        yield Fact(unusual_noise=self.input[4])
        yield Fact(car_vibrates=self.input[5])
        yield Fact(poor_braking=self.input[6])

    # def welcome_messages(self):
    #     print("Hi! I am here to help diagnose your car issues.")
    #     print("Please answer the following questions with 'yes' or 'no'.")

    # @Rule(Fact(action="find_issue"))
    # def find_car_issue(self):
    #     self.welcome_messages()
    #     self.declare_symptom("engine_start", "Engine won't start: ")
    #     self.declare_symptom("fuel_economy", "Poor fuel economy: ")
    #     self.declare_symptom("overheating", "Overheating: ")
    #     self.declare_symptom("excessive_exhaust_smoke",
    #                          "Excessive exhaust smoke: ")
    #     self.declare_symptom("unusual_noise", "Unusual noise: ")
    #     self.declare_symptom("car_vibrates", "Car vibrates: ")
    #     self.declare_symptom("poor_braking", "Poor braking performance: ")

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start="no"),
        Fact(fuel_economy="no"),
        Fact(overheating="no"),
        Fact(excessive_exhaust_smoke="no"),
        Fact(unusual_noise="no"),
        Fact(car_vibrates="no"),
        Fact(poor_braking="no")
    )
    def diagnose_issue_all_good(self):
        issue = "All Good To Go!!"
        self.declare(Fact(issue=issue))

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start="yes"),
        Fact(fuel_economy="yes"),
        Fact(overheating="yes"),
        Fact(excessive_exhaust_smoke="yes"),
        Fact(unusual_noise="yes"),
        Fact(car_vibrates="yes"),
        Fact(poor_braking="yes")
    )
    def diagnose_issue_all_bad(self):
        issue = "Mechanic Inspection Necessary!!"
        self.declare(Fact(issue=issue))

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start="yes"),
        Fact(fuel_economy="yes"),
        Fact(overheating="no"),
        Fact(excessive_exhaust_smoke="no"),
        Fact(unusual_noise="no"),
        Fact(car_vibrates="no"),
        Fact(poor_braking="no")
    )
    def diagnose_1(self):
        issue = "Faulty Spark Plugs"
        self.declare(Fact(issue=issue))

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start="no"),
        Fact(fuel_economy="yes"),
        Fact(overheating="no"),
        Fact(excessive_exhaust_smoke="no"),
        Fact(unusual_noise="no"),
        Fact(car_vibrates="no"),
        Fact(poor_braking="no")
    )
    def diagnose_2(self):
        issue = "Clogged Air Filter"
        self.declare(Fact(issue=issue))

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start="yes"),
        Fact(fuel_economy="no"),
        Fact(overheating="yes"),
        Fact(excessive_exhaust_smoke="yes"),
        Fact(unusual_noise="no"),
        Fact(car_vibrates="no"),
        Fact(poor_braking="no")
    )
    def diagnose_3(self):
        issue = "Leaking Head Gasket"
        self.declare(Fact(issue=issue))

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start="no"),
        Fact(fuel_economy="no"),
        Fact(overheating="yes"),
        Fact(excessive_exhaust_smoke="no"),
        Fact(unusual_noise="no"),
        Fact(car_vibrates="no"),
        Fact(poor_braking="no")
    )
    def diagnose_4(self):
        issue = "Faulty Radiator"
        self.declare(Fact(issue=issue))

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start="yes"),
        Fact(fuel_economy="yes"),
        Fact(overheating="no"),
        Fact(excessive_exhaust_smoke="yes"),
        Fact(unusual_noise="no"),
        Fact(car_vibrates="no"),
        Fact(poor_braking="no")
    )
    def diagnose_5(self):
        issue = "Malfunctioning Oxygen Sensor"
        self.declare(Fact(issue=issue))

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start="no"),
        Fact(fuel_economy="no"),
        Fact(overheating="no"),
        Fact(excessive_exhaust_smoke="no"),
        Fact(unusual_noise="no"),
        Fact(car_vibrates="no"),
        Fact(poor_braking="yes")
    )
    def diagnose_6(self):
        issue = "Worn Brake Pads"
        self.declare(Fact(issue=issue))

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start="no"),
        Fact(fuel_economy="no"),
        Fact(overheating="no"),
        Fact(excessive_exhaust_smoke="no"),
        Fact(unusual_noise="yes"),
        Fact(car_vibrates="no"),
        Fact(poor_braking="no")
    )
    def diagnose_7(self):
        issue = "Damaged Suspension Bushings"
        self.declare(Fact(issue=issue))

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start="no"),
        Fact(fuel_economy="no"),
        Fact(overheating="no"),
        Fact(excessive_exhaust_smoke="no"),
        Fact(unusual_noise="yes"),
        Fact(car_vibrates="no"),
        Fact(poor_braking="yes")
    )
    def diagnose_8(self):
        issue = "Unbalanced Tires/Wheels"
        self.declare(Fact(issue=issue))

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start="yes"),
        Fact(fuel_economy="no"),
        Fact(overheating="no"),
        Fact(excessive_exhaust_smoke="no"),
        Fact(unusual_noise="yes"),
        Fact(car_vibrates="yes"),
        Fact(poor_braking="no")
    )
    def diagnose_9(self):
        issue = "Worn Out Clutch"
        self.declare(Fact(issue=issue))

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start="no"),
        Fact(fuel_economy="yes"),
        Fact(overheating="no"),
        Fact(excessive_exhaust_smoke="no"),
        Fact(unusual_noise="no"),
        Fact(car_vibrates="yes"),
        Fact(poor_braking="no")
    )
    def diagnose_10(self):
        issue = "Faulty Fuel Pump"
        self.declare(Fact(issue=issue))

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start="yes"),
        Fact(fuel_economy="yes"),
        Fact(overheating="no"),
        Fact(excessive_exhaust_smoke="no"),
        Fact(unusual_noise="no"),
        Fact(car_vibrates="no"),
        Fact(poor_braking="no")
    )
    def diagnose_11(self):
        issue = "Faulty Ignition Coil"
        self.declare(Fact(issue=issue))

    @Rule(
        Fact(action="find_issue"),
        Fact(engine_start=MATCH.engine_start),
        Fact(fuel_economy=MATCH.fuel_economy),
        Fact(overheating=MATCH.overheating),
        Fact(excessive_exhaust_smoke=MATCH.excessive_exhaust_smoke),
        Fact(unusual_noise=MATCH.unusual_noise),
        Fact(car_vibrates=MATCH.car_vibrates),
        Fact(poor_braking=MATCH.poor_braking), salience=-999)
    
    def test(self, engine_start, fuel_economy, overheating, excessive_exhaust_smoke, unusual_noise, car_vibrates, poor_braking):
        symptoms = {
            "engine_start": engine_start,
            "fuel_economy": fuel_economy,
            "overheating": overheating,
            "excessive_exhaust_smoke": excessive_exhaust_smoke,
            "unusual_noise": unusual_noise,
            "car_vibrates": car_vibrates,
            "poor_braking": poor_braking
        }
        symptoms = {k for k, v in symptoms.items() if v == "yes"}
        closest_problem = self.find_closest_problem(symptoms)
        self.declare(Fact(issue_suggested=closest_problem))

        problem_frequencies = {
            "Faulty Spark Plugs": 100,
            "Clogged Air Filter": 80,
            "Leaking Head Gasket": 70,
            "Faulty Radiator": 60,
            "Malfunctioning Oxygen Sensor": 50,
            "Worn Brake Pads": 40,
            "Damaged Suspension Bushings": 30,
            "Unbalanced Tires/Wheels": 20,
            "Worn Out Clutch": 10,
            "Faulty Fuel Pump": 5,
            "Faulty Ignition Coil": 2
        }
        items = list(problem_frequencies.items())
        items.sort(key=lambda x: x[1], reverse=True)
        L = [item[0] for item in items]
        self.result = ""
        a = ''
        issues = []
        for fact_id in self.facts:
            fact = self.facts[fact_id]
            if 'issue' in fact:
                issues.append(fact['issue'])
            if 'issue_suggested' in fact:
                a = fact['issue_suggested']
        if len(issues) > 1:
            self.result= self.result + f"You could have any of these issues: {', '.join(issues)}"
            issues.sort(key=lambda x: L.index(x))
            self.result= self.result +f"\n But probably your issue is: {issues[0]}"
        elif issues:
            if issues[0] == "All Good To Go!!":
                self.result= self.result +"All Good To Go!!"
            elif issues[0] == "Mechanic Inspection Necessary!!":
                self.result= self.result +"Mechanic Inspection Necessary!!"
            else:
                self.result= self.result +f"The most probable car issue is: {issues[0]}"
        elif len(issues) == 0:
            self.result= self.result +f"The closest car issue is: {a}"
        


# if __name__ == "__main__":
#     engine = CarDiagnostic()
#     engine.reset()
#     engine.run()

#     problem_frequencies = {
#         "Faulty Spark Plugs": 100,
#         "Clogged Air Filter": 80,
#         "Leaking Head Gasket": 70,
#         "Faulty Radiator": 60,
#         "Malfunctioning Oxygen Sensor": 50,
#         "Worn Brake Pads": 40,
#         "Damaged Suspension Bushings": 30,
#         "Unbalanced Tires/Wheels": 20,
#         "Worn Out Clutch": 10,
#         "Faulty Fuel Pump": 5,
#         "Faulty Ignition Coil": 2
#     }

#     items = list(problem_frequencies.items())
#     items.sort(key=lambda x: x[1], reverse=True)
#     L = [item[0] for item in items]

#     issues = []
#     for fact_id in engine.facts:
#         fact = engine.facts[fact_id]
#         if 'issue' in fact:
#             issues.append(fact['issue'])

#     if len(issues) > 1:
#         print(f"You could have any of these issues: {', '.join(issues)}")
#         issues.sort(key=lambda x: L.index(x))
#         print(f"But probably your issue is: {issues[0]}")
#     elif issues:
#         if issues[0] == "All Good To Go!!":
#             print("All Good To Go!!")
#         elif issues[0] == "Mechanic Inspection Necessary!!":
#             print("Mechanic Inspection Necessary!!")
#         else:
#             print(f"The most probable car issue is: {issues[0]}")