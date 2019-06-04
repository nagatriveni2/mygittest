#OOPR-Assgn-20
#Start writing your code here
class applicant:
    applicant_dict={'A':0,'B':0,'C':0}
    applicant_id_count=1000
    applicant_id=1001
    applicant_name=""
    job_band=['A','B','C']
    def __init__(self,applicant_name):
        self.applicant_name=applicant_name
    def generate_applicant_id(self):
        self.applicant_id=self.applicant_id+1
    def apply_for_job(self,job):
	self.generate_applicant_id()
        for i in applicant_dict.keys():
            if(i==job):
                v=self.applicant_dict.get(i)
                if(v<=5):
                    self.applicant_id_count=self.applicant_id_count+1
                    v=v+1
                    d1={job:v}
                    self.applicant_dict.update(d1)
                    print(self.applicant_dict.items())
                    print(self.get_application_id())
                    print(self.get_applicant_name())
                    print(self.get_application_id())
                    print(self.get_application_dict())
		    return True
		    
                else:
                    return -1
    def get_application_dict(self):
        return self.applicant_dict
    def get_application_id(self):
        return self.applicant_id
    def get_applicant_name(self):
        return self.applicant_name
    def get_job_band(self):
        return self.job
        
applicant_dict={'A':0,'B':0,'C':0}
c1=applicant("john")
c1.apply_for_job('A')

            
            
            
            
            
            
            
            
        
