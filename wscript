def configure(conf):
    conf.load('gcc')

# This fails with: "source not found: 'waf-fail.o'"
def build(bld):
    bld.objects(source='waf-fail.c', target='waf-fail.o')
    bld.program(source='waf-fail.o', target='waf-fail')

# For reference, this succeeds
#def build(bld):
#    bld(rule="${CC} -c ${SRC} -o ${TGT}", source='waf-fail.c', target='waf-fail.o')
#    bld(rule="${CC} ${SRC} -o ${TGT}", source='waf-fail.o', target='waf-fail')


# vim:filetype=python