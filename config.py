###
# Copyright (c) 2011, Clint Savage
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Irc2rss', True)



Irc2rss = conf.registerPlugin('Irc2rss')

conf.registerChannelValue(Irc2rss, 'basepath', registry.String("/tmp/Irc2rss", """Base path of the rss data"""))
conf.registerChannelValue(Irc2rss, 'title', registry.String("IRC2RSS Feed for %(user)s", """Title of the generated RSS feed"""))
conf.registerChannelValue(Irc2rss, 'link', registry.String("http://irc2rss.org/feed/%(user)s/rss.xml", """URL of your site or blog"""))
conf.registerChannelValue(Irc2rss, 'description', registry.String("This feed is generated by the Supybot plugin, Irc2rss. More information is available at http://github.com/herlo/supybot-irc2rss/", """Description of this feed"""))
conf.registerChannelValue(Irc2rss, 'dateFormat', registry.String("%m/%d%Y %H:%M", """Date format printed in rss feed"""))

# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(Irc2rss, 'someConfigVariableName',
#     registry.Boolean(False, """Help for someConfigVariableName."""))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
