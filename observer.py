App.focus("FieldWorks")
def changed(event):
        print "something changed in ", event.region
        for ch in event.changes:
                ch.highlight() # highlight all changes
        sleep(1)
        for ch in event.changes:
                ch.highlight() # turn off the highlights

r = selectRegion()
print "region is", r
r.onChange(5000, changed)
r.observe(background=True)

wait(30) # another way to observe for 30 seconds
r.stopObserver()

