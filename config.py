# database info
dbname = 'foodnow'
dbuser = 'postgres'
dbpass = 'hello123'

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

# employee roles
rolemanager = 10
roleworker = 5
roledriver = 1
roles = [(rolemanager, 'Manager'), (roleworker, 'Worker'), (roledriver, 'Driver')]