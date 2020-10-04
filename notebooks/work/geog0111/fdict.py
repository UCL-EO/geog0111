

def fdict(idict,ignore=[]):
  '''return partial version of idict'''
  this = idict
  dellist = []
  for k,v in this.items():
    if (k[:len('_cached')] == '_cached'):
      dellist.append(k)
    if k == 'store_msg':
      dellist.append(k)
    if k in ignore:
      dellist.append(k)
  for k in dellist:
    del this[k]
  this['store_msg'] = []
  return this

