import os

# database info
dbname = environ['fn_dbname'] if 'fn_dbname' in os.environ else 'foodnow'
dbuser = environ['fn_dbuser'] if 'fn_dbuser' in os.environ else 'postgres'
dbpass = environ['fn_dbpass'] if 'fn_dbpass' in os.environ else 'hello123'

# lengths needed
namemin = 3
namemax = 32
mailmin = 8
mailmax = 64
passwordmin = 3
passwordmax = 64

restonamemin = 4
restonamemax = 64
restopseudomin = 3
restopseudomax = 16
restowarnmsgmax = 512
restodescriptionmax = 512

menunamemin = 3
menunamemax = 16
dishnamemin = 3
dishnamemax = 24
dishdescriptionmax = 256

dishpctsize = (1014, 768)
dishthumbsize = (128, 64)

# employee roles
rolemanager = 10
roleworker = 5
roledriver = 1
roles = [(rolemanager, 'Manager'), (roleworker, 'Worker'), (roledriver, 'Driver')]

# file extensions
pctextensions = set(['png', 'jpg', 'jpeg', 'gif'])

# upload paths
dishespctpath = 'uploads/dishes/'
dishesthumbspath = 'uploads/dishes/thumbs/'

phones = ['phone', 'android', 'blackberry', 'mobile']