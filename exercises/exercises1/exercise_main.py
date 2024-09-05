
from exercise_classes import Report,Contract,Presentation

if __name__ == "__main__":
    
    report_template = Report("Annual Report","Content of the annual report.","Alex Mus")
    contract_template = Contract("Rent Contract","Content of the Rent Contract","Alex Mus")
    presentation_template = Presentation("Projectpresentation", "Content of Presentation", "Alex Mus")

    print(report_template)
    print(contract_template)
    print(presentation_template)
    

    new_doc = report_template.clone()
    new_doc.set_type("Presentation")
    print(new_doc)
