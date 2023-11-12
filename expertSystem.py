from experta import *


class CarDiagnostic(KnowledgeEngine):
    def __init__(self , input):
        super().__init__()
        self.input=input
        
    
    def declare_symptom(self, symptom_name, question):
        user_input = input(question)
        # Create a dictionary with the symptom_name as the key
        fact_dict = {symptom_name: user_input}
        # Use the ** operator to unpack the dictionary into a Fact
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

    # @Rule(Fact(action="find_issue"),salience=-1)
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

    # ... rules ...
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
        issue = "All is bad innit"
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
        issue = "Damages Suspensions Bushings"
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
        issue = "Unbalanced Tires"
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
        Fact(engine_start="no"),
        Fact(fuel_economy="no"),
        Fact(overheating="yes"),
        Fact(excessive_exhaust_smoke="no"),
        Fact(unusual_noise="no"),
        Fact(car_vibrates="no"),
        Fact(poor_braking="no")
)
    def diagnose_11(self):
        issue = "Faulty Ignition Coil"
        self.declare(Fact(issue=issue))
    @Rule(NOT(Fact(issue=MATCH.issue)), salience=-1)
    def no_issue_detected(self):
        self.declare(Fact(issue="No issue detected"))
    #--------------------------------------------------------------------------------
    @Rule(Fact(issue=MATCH.issue))
    def diagnose_issue(self, issue):
        self.result = issue
# if __name__ == "__main__":
#     engine = CarDiagnostic()
#     engine.reset()
#     engine.run()

    # if "issue" in engine.facts.keys():
    #     issue = engine.facts["issue"]
    #     print(f"The most probable car issue is: {issue}")
    # f = engine.facts
    # print(f['issue']