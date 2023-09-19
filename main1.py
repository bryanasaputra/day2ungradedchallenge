#Ungraded part 1
customer_id = ['B818', 'A461', 'A092', 'A082', 'B341', 'A005',
                'A092', 'A461','B219', 'B904', 'A901', 'A083',
                  'B904', 'A092', 'B341', 'B821','B341', 'B821',
                    'B904', 'B818', 'A901', 'A083', 'B818', 'A082',
                    'B219', 'B219', 'A083', 'A901', 'A082', 'B341',
                      'B341', 'A083','A082', 'B219', 'B439', 'A461',
                        'A005', 'A901', 'B341', 'A082','A083', 'A461',
                          'A083', 'A901', 'A461', 'A083', 'A082', 'A083',
                          'B341', 'A901', 'A082', 'A461', 'B219', 'A083',
                            'B818', 'B821','A092', 'B341', 'A461', 'A092',
                              'A083', 'B821', 'A092']

#How many unique customer_id from above list?
setcalc=set(customer_id)
unique_customerid = len(setcalc)
print(f"There is {unique_customerid} unique number in the list above")