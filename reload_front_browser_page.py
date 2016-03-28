from Foundation import *

if __name__ == '__main__': # main call
	
	reloadPage = '''
	tell application "Safari"
    set docUrl to URL of document 1
    set URL of document 1 to docUrl
	end tell'''

	appleScript = NSAppleScript.alloc().initWithSource_(reloadPage)
	appleScriptError = appleScript.executeAndReturnError_(None)
	if appleScriptError[1] != None:
		print(appleScriptError)
		exit(-1)
