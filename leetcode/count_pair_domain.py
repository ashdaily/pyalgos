"""
https://leetcode.com/problems/subdomain-visit-count/submissions/
"""

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        cpdomains_data = {}
        
        for cpdomain in cpdomains:
            visit_counts ,full_domain = cpdomain.split()
            
            visit_counts = int(visit_counts)
            
            if full_domain.count(".") == 2:
                subdomain, domain, tld = full_domain.split(".")
            
            if full_domain.count(".") == 1:
                subdomain = None
                domain, tld = full_domain.split(".")

                    
            if tld in cpdomains_data.keys():
                cpdomains_data[tld] += visit_counts
            else:
                cpdomains_data[tld] = visit_counts
            
            if f"{domain}.{tld}" in cpdomains_data.keys():
                cpdomains_data[f"{domain}.{tld}"] += visit_counts
            else:
                cpdomains_data[f"{domain}.{tld}"] = visit_counts
                
            if subdomain:
                if full_domain in cpdomains_data.keys():
                     cpdomains_data[full_domain] += visit_counts
                else:
                    cpdomains_data[full_domain] = visit_counts
        
        
        return [f"{v} {k}" for k,v in cpdomains_data.items()]
                    
                    
        
        
            
            
            
            
            
            
            
        