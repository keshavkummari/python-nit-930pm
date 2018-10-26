#!/usr/bin/python

d1 = {'Name': 'minnu', 'Age': 7}

print ("Value : %s" %  d1.has_key('Age'))
print ("Value : %s" %  d1.has_key('Gender'))


"""
[root@reposerver ~]# python --version
Python 2.7.5

[root@reposerver ~]# cat has_keys.py
#!/usr/bin/python

dict = {'Name': 'minnu', 'Age': 7}

print ("Value : %s" %  dict.has_key('Age'))
print ("Value : %s" %  dict.has_key('Gender'))

[root@reposerver ~]# python has_keys.py
Value : True
Value : False
[root@reposerver ~]#
"""
