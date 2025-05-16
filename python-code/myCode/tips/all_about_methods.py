def example_method(mandatory_parameter, default_parameter = "Default", *variable_parameter, **key_word_args):
    print(f"""
          mandatory_parameter = {mandatory_parameter} {type(mandatory_parameter)}
          default_parameter = {default_parameter} {type(default_parameter)}
          variable_parameter = {variable_parameter} {type(variable_parameter)}
          keyword_parameter = {key_word_args} {type(key_word_args)}
          """)

#example_method()  #compilation error: missing required positional argument
example_method(15)
example_method(mandatory_parameter=15)
example_method(15,45)
example_method(15, "some string")
example_method("string1", "string2", "string3", "string4", "string5")
example_method("string1", "string2", "string3", "string4", "string5", key1='a', key2='b')
example_method("string1", "string2",  key1='a', key2='b')

values = [1,2,3,4,5,6]
example_method(values[0], values[1], values[2],values[3], values[4], values[5])
example_method(*values)
dictionary = {'a':'1','b':'2','c':'3','d':'4','e':'5'}
example_method(*values,**dictionary)