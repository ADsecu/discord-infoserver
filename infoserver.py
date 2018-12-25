import os
import sys
import discord
import logging
import asyncio
import time
import datetime


token = "Token Here"


bot =  discord.Client()
are_you_windows = os.name == "nt"
file = "{} - {}.html"
html = []

help_note = """
 ___ _   _ _____ ___
|_ _| \ | |  ___/ _ \ ___  ___ _ ____   _____ _ __
 | ||  \| | |_ | | | / __|/ _ \ '__\ \ / / _ \ '__|
 | || |\  |  _|| |_| \__ \  __/ |   \ V /  __/ |
|___|_| \_|_|   \___/|___/\___|_|    \_/ \___|_| v0.0.2
#=====================================================#
#                  Twitter: @ADsecu                   #
#=====================================================#

"""

help_note2 = """
 Choose :
  [1]  Analysis All servers You have.
  [2]  Analysis server by ID.
  [3]  List all server You have
  [0]  Exit
  [00] Clear screen ;)
"""

def clear_screen():
    if are_you_windows:
        os.system("cls")
    else:
        os.system("clear")



@bot.event
async def on_ready():
    clear_screen()
    print(help_note)
    print('\n')
    print('---------------------')
    print('I  AM  ONLINE')
    print("MY  NAME  IS:   @" + bot.user.name + "#" + bot.user.discriminator)
    print("MY  ID  IS: "+ bot.user.id)
    print('---------------------\n')

    print(help_note2)
    while 1+1 != 3:
        inp = input('INFOserver~$ ')
        if inp == '1':
            print('WORKING ... ')
            for server in bot.servers:
                server = discord.utils.get(bot.servers, id=server.id)
                _main(server)
                print('\33[32m[+]Success: {} \33[0m'.format(server.id))
                html.clear()
            print('{} servers / All Data saved as HTML file in folder'.format(len(bot.servers)))

        elif inp == '2':
            serverid = input('Type or Paste server ID $~ ')
            server = discord.utils.get(bot.servers, id=serverid)
            if server:
                _main(server)
                print('\33[32m[+]Success: {}\33[0m'.format(server.id))
                html.clear()
                print('Data saved as HTML file in folder')
            else:
                print('\033[91mInvalid Server ID\033[0m')

        elif inp == '3':
            count = 1
            for server in bot.servers:
                print('{} - Server ID :{} | OWNER : ({})'.format(count, server.id, server.owner))
                count = count + 1
        elif inp == '0':
            print('Force Close Connection .. Thanks ')
            sys.exit()
        elif inp == '00':
                clear_screen()
                print(help_note)
                print('\n')
                print('---------------------')
                print('I  AM  ONLINE')
                print("MY  NAME  IS:   @" + bot.user.name + "#" + bot.user.discriminator)
                print("MY  ID  IS: "+ bot.user.id)
                print('---------------------\n')
                print(help_note2)
        else:
            print('\033[91mERORR\033[0m\n[0] to Exit\n[00] For Clear screen & Home ')





def html_generate():
    html.append("""<HEAD>
<meta charset="UTF-8">
<TITLE>INFOserver</TITLE>
</HEAD>
<BODY BGCOLOR="ECECE9">
<h1 style="text-align: center;"><img src="https://i.imgur.com/nAKGaKu.png" alt="" width="219" height="147" /></h1>
<h1 style="text-align: center;"><span style="background-color: #999999;">infoserver</span>&nbsp;to analysis servers&nbsp;</h1>
<p style="text-align: center;">This code made with <span style="background-color: #ff0000;">&lt;3</span> by free time :)</p>
<p style="text-align: center;">*Github page <a href="https://github.com/ADsecu">ADsecu</a></p>
<p style="text-align: center;">*Twitter page <a href="http://twitter.com/adsecu">@ADsecu</a></p>
<p style="text-align: center;">*For support <a title="Support" href="https://www.google.com" target="_blank" rel="noopener">click here</a></p>
""")
    html.extend('<p style="text-align: center;"><span style="text-decoration: underline; background-color: #999999;"><em>Time : {}</em></span></p>\n<p>&nbsp;</p>\n'
                '<p>&nbsp;</p>\n'
                '<p>&nbsp;</p>\n'.format(datetime.datetime.now().strftime("%I:%M%p | %d/%m/%Y")))

    html.extend("""
<h2>Quick &amp; Click&nbsp;</h2>
<table style="height: 389px; width: 641px; border-color: #000000; float: left;" border="--">
<tbody>
<tr style="height: 157.84375px;">
<td style="width: 206.296875px; height: 157.84375px;">
<p><a href="#members">Members:</a></p>
<ul>
<li><a href="#administrator">administrator</a></li>
<li><a href="Ban_members">ban_members</a></li>
<li><a href="#kick_members">kick_members</a></li>
<li><a href="#manage_server">manage_server</a></li>
<li><a href="#manage_roles">manage_roles</a></li>
<li><a href="#manage_channels">manage_channels</a></li>
<li><a href="#manage_messages">manage_messages</a></li>
</ul>
<p><a href="#roles">Roles:</a></p>
<ul>
<li><a href="#top10">Top 10 roles with members</a></li>
<li><a href="#rolespermissions">Roles permissions</a></li>
</ul>
<p>&nbsp;</p>
</td>
<td style="width: 217.703125px; height: 157.84375px;">
<p><a href="#channels">Channels:</a></p>
<ul>
<li><a href="#hidden_text_channels">Hidden text channels</a></li>
<li><a href="#Muted_roles">Muted roles in channels</a></li>
<li><a href="#Muted_members">Muted members in channels</a></li>
<li><a href="#hidden_voice_channels">Hidden voice channels</a></li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
    """)

def _info(server):
    html.extend("""<h1 id='info'>== General info == </h1>
    """)
    members = len([member for member in server.members if not member.bot])
    bots = len([member for member in server.members if member.bot])

    server_ginfo =  ('<blockquote>\n'
                    '<h2><img style="font-size: 14px;" src="{}" alt="server icon" width="105" height="105" /></h2>\n'
                    '<table style="height: 43px; width: 432px; background-color: #dde7a4; float: left;">\n'
                    '<tbody>\n'
                    '<tr style="height: 34px;">\n'
                    '<td style="width: 138.5px; height: 34px;">Server owner</td>\n'
                    '<td style="width: 282.5px; height: 34px;">@{}</td>\n'
                    '</tr>'
                    '<tr style="height: 26px;">\n'
                    '<td style="width: 138.5px; height: 26px;">Server ID</td>\n'
                    '<td style="width: 282.5px; height: 26px;">{}</td>\n'
                    '</tr>'
                    '<tr style="height: 26.375px;">\n'
                    '<td style="width: 138.5px; height: 26.375px;">Server name</td>\n'
                    '<td style="width: 282.5px; height: 26.375px;">{}</td>\n'
                    '</tr>\n'
                    '<tr style="height: 26.375px;">\n'
                    '<td style="width: 138.5px; height: 26.375px;">Members</td>\n'
                    '<td style="width: 282.5px; height: 26.375px;">{}</td>\n'
                    '</tr>\n'
                    '<tr style="height: 26.375px;">\n'
                    '<td style="width: 138.5px; height: 26.375px;">Bots</td>\n'
                    '<td style="width: 282.5px; height: 26.375px;">{}</td>\n'
                    '</tr>\n'
                    '</tbody>\n'
                    '</table>\n'
                    '<p>&nbsp;</p>\n'
                    '</blockquote>\n'
                    '<p style="text-align: left;">&nbsp;</p>\n'
                    '<p>&nbsp;</p>\n'
                    '<p>&nbsp;</p>\n'
                    '<p>&nbsp;</p>\n'
                    '<p>&nbsp;</p>\n'.format(server.icon_url, server.owner, server.id, server.name, members, bots))

    html.extend(server_ginfo)
    member_has_muted_role(server)
    my_permissions(server)


def my_permissions(server):
    inv = []
    move = []
    manage = []
    roles = []
    mmessages = []

    for channel in server.channels:
        if channel.type == discord.ChannelType.voice:
            if (channel.permissions_for(server.me).create_instant_invite or
                                        channel.permissions_for(server.me).create_instant_invite == True):
                inv.append(channel.name)

            if (channel.permissions_for(server.me).move_members or
                                       channel.permissions_for(server.me).move_members == True):
                move.append(channel.name)

            if (channel.permissions_for(server.me).manage_channels or
                                       channel.permissions_for(server.me).manage_channels == True):
                manage.append(channel.name)
            if (channel.permissions_for(server.me).manage_roles or
                                       channel.permissions_for(server.me).manage_roles == True):
                roles.append(channel.name)

        if channel.type == discord.ChannelType.text:
            if (channel.permissions_for(server.me).create_instant_invite or
                                        channel.permissions_for(server.me).create_instant_invite == True):
                inv.append(channel.name)

            if (channel.permissions_for(server.me).manage_channels or
                                       channel.permissions_for(server.me).manage_channels == True):
                manage.append(channel.name)

            if (channel.permissions_for(server.me).manage_roles or
                                       channel.permissions_for(server.me).manage_roles == True):
                roles.append(channel.name)

            if (channel.permissions_for(server.me).manage_messages or
                                                   channel.permissions_for(server.me).manage_messages == True):
                mmessages.append(channel.name)


    yr_perm = ('<p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><h2>== Your permissions in server ==</h2>'
                        '<p>*Note: These permissions have been searched deeply in all channels</p>'
                        '\n')

    html.extend(yr_perm)
    html.extend("<ul>\n")
    if server.me.server_permissions.administrator:
        administrator = '<li>administrator = <u>True</u></li>\n'
        html.extend(administrator)
    else:
        administrator = '<li>administrator = <u>False</u></li>\n'
        html.extend(administrator)
        if server.me.server_permissions.manage_server:
            manage_s = '<li>manage_server = <u>True</u></li>\n'
            html.extend(manage_s)
        else:
            manage_s = '<li>manage_server = <u>False</u></li>\n'
            html.extend(manage_s)
        if server.me.server_permissions.mute_members:
            mute_m = '<li>mute_members = <u>True</u></li>\n'
            html.extend(mute_m)
        else:
            mute_m = '<li>mute_members = <u>False</u></li>\n'
            html.extend(mute_m)
        if len(inv) > 0:
            invite = '<li>create_invite = <span style="text-decoration: underline;">True&nbsp;</span>| {}</li>\n'.format(inv)
            html.extend(invite)
        else:
            invite = "<li>create_invite = <u>False</u></li>\n"
            html.extend(invite)
        if len(move) >0:
            move_m = '<li>move_members = <span style="text-decoration: underline;">True&nbsp;</span>| {}</li>\n'.format(move)
            html.extend(move_m)
        else:
            move_m = "<li>move_members = <u>False</u></li>\n"
            html.extend(move_m)
        if len(manage) >0:
            manage_c = '<li>manage_channels = <span style="text-decoration: underline;">True&nbsp;</span>| {}</li>\n'.format(manage)
            html.extend(manage_c)
        else:
            manage_c = "<li>manage_channels = <u>False</u></li>\n"
            html.extend(manage_c)
        if len(roles) >0:
            manage_r = '<li>manage_roles = <span style="text-decoration: underline;">True&nbsp;</span>| {}</li>\n'.format(roles)
            html.extend(manage_r)
        else:
            manage_r = "<li>manage_roles = <u>False</u></li>\n"
            html.extend(manage_r)
        if len(mmessages) >0:
            manage_m = '<li>manage_messages = <span style="text-decoration: underline;">True&nbsp;</span>| {}</li>\n'.format(mmessages)
            html.extend(manage_m)
        else:
            manage_m = "<li>manage_messgaes = <u>False</u></li>\n"
            html.extend(manage_m)
    html.extend("</ul>\n")

    me_roles = ' <strong> - </strong> '.join([role.name for role in server.roles if role in server.me.roles and role != server.default_role])
    if len(me_roles) >0:
        html.extend('<p><strong>Roles : </strong>{}</p>\n'.format(me_roles))
    else:
        html.extend('<p><strong>Roles : </strong>None</p>\n')

def _administrator(server):
    html.extend("""<h2 id='administrator'><span style="background-color: #ff0000;">Administrator = True</span></h2>
    """)
    members_admins  = "\n".join(['<li>@' +member.name + '#' + member.discriminator + '</li>\n' for member in server.members if member.server_permissions.administrator
                                        if member != server.owner and member.bot == False])
    bot_admins = "\n".join(['<li>@' + member.name + '#' + member.discriminator + '</li>\n' for member in server.members if member.server_permissions.administrator
                                        and member.bot])

    html.extend("<h3>Users</h3>\n")
    if len(members_admins) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(members_admins))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend('<h3>Bots</h3>\n')
    if len(bot_admins) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(bot_admins))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')






def _ban(server):
    html.extend("""<h2 id = 'Ban_members'><span style="background-color: #ff6600;">Ban_members = True</span></h2>
    """)
    members_ban  = "\n".join(['<li>@' +member.name + '#' + member.discriminator + '</li>' for member in server.members
                             if member.server_permissions.ban_members == True and member.server_permissions.administrator == False
                             and member.bot == False])
    bot_ban = '\n'.join(['<li>@' +member.name + '#' + member.discriminator + '</li>' for member in server.members
                         if member.server_permissions.ban_members == True and member.server_permissions.administrator == False
                         and member.bot ])

    html.extend("<h3>Users</h3>\n")
    if len(members_ban) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(members_ban))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend('<h3>Bots</h3>\n')
    if len(bot_ban) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(bot_ban))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')


def _kick(server):
    html.extend("""<h2 id ='kick_members'><span style="background-color: #ff9900;">kick_members = True</span></h2>
    """)
    members_kick  = "\n".join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in server.members
                             if member.server_permissions.kick_members == True and member.server_permissions.administrator == False
                             and member.bot == False])
    bot_kick = '\n'.join(['<li>@' +member.name + '#' + member.discriminator + '</li>' for member in server.members
                         if member.server_permissions.kick_members == True and member.server_permissions.administrator == False
                         and member.bot ])
    html.extend("<h3>Users</h3>\n")
    if len(members_kick) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(members_kick))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend('<h3>Bots</h3>\n')
    if len(bot_kick) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(bot_kick))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')


def _manage_server(server):
    html.extend("""<h2 id='manage_server'><span style="background-color: #ffcc00;">manage_server = True</span></h2>
    """)
    members_m_server = "\n".join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in server.members
                             if member.server_permissions.manage_server == True and member.server_permissions.manage_server == False
                             and member.bot == False])
    bot_m_server = "\n".join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in server.members
                             if member.server_permissions.manage_server == True and member.server_permissions.manage_server == False
                             and member.bot])
    html.extend("<h3>Users</h3>\n")
    if len(members_m_server) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(members_m_server))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend('<h3>Bots</h3>\n')
    if len(bot_m_server) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(bot_m_server))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')

def _manage_roles(server):
    html.extend("""<h2 id="manage_roles"><span style="background-color: #ffcc99;">manage_roles = True</span></h2>
    """)
    members_roles = '\n'.join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in server.members
                                if member.server_permissions.manage_roles == True and member.server_permissions.administrator == False
                                and member.bot == False])
    bot_roles = '\n'.join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in server.members
                                if member.server_permissions.manage_roles == True and member.server_permissions.administrator == False
                                and member.bot])
    html.extend("<h3>Users</h3>\n")
    if len(members_roles) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(members_roles))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend("<h3>Bots</h3>\n")
    if len(bot_roles) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(bot_roles))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')



def _manage_channels(server):
    html.extend("""<h2 id = "manage_channels"><span style="background-color: #ffff99;">manage_channels = True</span></h2>
    """)

    members_channels = '\n'.join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in server.members
                                if member.server_permissions.manage_channels == True and member.server_permissions.administrator == False
                                and member.bot == False])
    bot_channels = '\n'.join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in server.members
                                if member.server_permissions.manage_channels == True and member.server_permissions.administrator == False
                                and member.bot])
    html.extend("<h3>Users</h3>\n")
    if len(members_channels) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(members_channels))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend("<h3>Bots</h3>\n")
    if len(bot_channels) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(bot_channels))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')

def _manage_messages(server):
    html.extend("""<h2 id="manage_messages"><span style="background-color: #339966;">manage_messages = True</span></h2>
    """)

    members_messages = '\n'.join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in server.members
                                if member.server_permissions.manage_messages == True and member.server_permissions.administrator == False
                                and member.bot == False])
    bot_messages = '\n'.join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in server.members
                                if member.server_permissions.manage_messages == True and member.server_permissions.administrator == False
                                and member.bot])
    html.extend("<h3>Users</h3>\n")
    if len(members_messages) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(members_messages))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend("<h3>Bots</h3>\n")
    if len(bot_messages) > 0:
        html.extend('<ul>\n')
        html.extend("{}".format(bot_messages))
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')


def _check_roles_members(server):
    html.extend("""<h2 id='top10'>Top <span style="text-decoration: underline;">10</span> roles with members</h2>
    """)
    count = 0
    msg_toappend = ""
    for role in server.role_hierarchy:
        if count < 10:
            count += 1
            m_roles = '\n'.join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in server.members if role in member.roles
                                and member.bot == False])
            b_roles = '\n'.join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in server.members if role in member.roles
                                and member.bot])

            msg_toappend += '<h3><span style="background-color: #bdbcb9; color: {};">{}</span></h3>\n'.format(role.color, role.name)
            msg_toappend += '<p>[Users]</p>\n'
            if len(m_roles) >0:
                msg_toappend += '<ul>\n'
                msg_toappend += "{}\n".format(m_roles)
                msg_toappend += '</ul>\n'
            else:
                msg_toappend += '<p><span style="text-decoration: underline;">NONE</span></p>\n'
            msg_toappend += '<p>[Bots]</p>\n'
            if len(b_roles) >0:
                msg_toappend += '<ul>\n'
                msg_toappend += "{}\n".format(b_roles)
                msg_toappend += '</ul>\n'
            else:
                msg_toappend += '<p><span style="text-decoration: underline;">NONE</span></p>\n'
    html.extend(msg_toappend)



def _check_roles_permissions(server):
    html.extend("""<h2 id='rolespermissions'>Roles permissions</h2>
    """)


    role_admin = "\n".join(['<li>' + role.name + '</li>' for role in server.role_hierarchy if role.permissions.administrator])
    role_ban_members = "\n".join(['<li>' + role.name + '</li>' for role in server.role_hierarchy if role.permissions.ban_members])
    role_kick_members = "\n".join(['<li>' + role.name + '</li>' for role in server.role_hierarchy if role.permissions.kick_members])
    role_m_server = "\n".join(['<li>' + role.name + '</li>' for role in server.role_hierarchy if role.permissions.manage_server])
    role_m_channels = "\n".join(['<li>' + role.name + '</li>' for role in server.role_hierarchy if role.permissions.manage_channels])
    role_m_roles = "\n".join(['<li>' + role.name + '</li>' for role in server.role_hierarchy if role.permissions.manage_roles])
    role_m_messages = "\n".join(['<li>' + role.name + '</li>' for role in server.role_hierarchy if role.permissions.manage_messages])
    role_move_member = "\n".join(['<li>' + role.name + '</li>' for role in server.role_hierarchy if role.permissions.move_members])
    role_mute_member = "\n".join(['<li>' + role.name + '</li>' for role in server.role_hierarchy if role.permissions.mute_members])
    role_create_invite = "\n".join(['<li>' + role.name + '</li>' for role in server.role_hierarchy if role.permissions.create_instant_invite])

    html.extend('<p><strong>Administrator</strong></p>\n')
    if len(role_admin) >0:
        html.extend('<ul>\n')
        html.extend(role_admin)
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend('<p><strong>ban_members</strong></p>\n')
    if len(role_ban_members) >0:
        html.extend('<ul>\n')
        html.extend(role_ban_members)
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend('<p><strong>kick_members</strong></p>\n')
    if len(role_kick_members) >0:
        html.extend('<ul>\n')
        html.extend(role_kick_members)
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend('<p><strong>manage_server</strong></p>\n')
    if len(role_m_server)>0:
        html.extend('<ul>\n')
        html.extend(role_m_server)
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend('<p><strong>manage_channels</strong></p>\n')
    if len(role_m_channels) >0:
        html.extend('<ul>\n')
        html.extend(role_m_channels)
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend('<p><strong>manage_roles</strong></p>\n')
    if len(role_m_roles) >0:
        html.extend('<ul>\n')
        html.extend(role_m_roles)
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend('<p><strong>manage_messages</strong></p>\n')
    if len(role_m_messages) >0:
        html.extend('<ul>\n')
        html.extend(role_m_messages)
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend('<p><strong>move_members</strong></p>\n')
    if len(role_move_member) >0:
        html.extend('<ul>\n')
        html.extend(role_move_member)
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend('<p><strong>mute_members</strong></p>\n')
    if len(role_mute_member) >0:
        html.extend('<ul>\n')
        html.extend(role_mute_member)
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')
    html.extend('<p><strong>create_invite</strong></p>\n')
    if len(role_create_invite) >0:
        html.extend('<ul>\n')
        html.extend(role_create_invite)
        html.extend('</ul>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')








def _tc(server):
    html.extend("""<h2 id='hidden_text_channels'>Hidden channels</h2>
    """)
    hidden_text_channels = "\n".join(['<li>#' + channel.name + ' &nbsp;| &nbsp;' + channel.id + '</li>' for channel in server.channels if channel.type == discord.ChannelType.text
                                    and channel.permissions_for(server.me).read_messages == False])
                                    # (server.me) return False , as a bot or user permissions

    if len(hidden_text_channels) > 0:
        html.extend('<ol>\n')
        html.extend(hidden_text_channels)
        html.extend('</ol>\n')
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')



def _vm(server):
    html.extend("""<h2 id='hidden_voice_channels'>Hidden voice channels with members</h2>
    """)
    log_for_html = []
    for channel in server.channels:
            if channel.type == discord.ChannelType.voice:
                if channel.permissions_for(server.me).connect == False:
                    voice_channel = discord.utils.get(server.channels, id = channel.id)
                    members = voice_channel.voice_members
                    member_names = '\n'.join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in members])
                    add_10 = "<p><strong>&gt; {} :</strong></p>\n<ol>{}</ol>\n".format(voice_channel.name, member_names)
                    log_for_html.extend(add_10)
    if len(log_for_html) >0:
        for m in log_for_html:
            html.extend(m)
    else:
        html.extend('<p><span style="text-decoration: underline;">NONE</span></p>\n')


def role_check_channels_permissionsFalse(server):
    html.extend("""<h2 id='Muted_roles'>Muted roles in channels</h2>
    """)
    for channel in server.channels:
        if channel.type == discord.ChannelType.text:
            chat = ' - '.join([role.name for role in server.roles if channel.overwrites_for(role).send_messages == False and
                                channel.overwrites_for(role).read_messages == None and role != server.default_role])
            if len(chat) > 0:
                html.extend("<p><strong>#{}</strong> | {}</p>\n".format(channel.name, chat))
            else:
                html.extend('<p><strong>#{}</strong> | NONE</p>\n'.format(channel.name))

def member_check_channels_permissionsFalse(server):
    html.extend("""<h2 id="Muted_members">Muted members in channels</h2>
    """)
    for channel in server.channels:
        if channel.type == discord.ChannelType.text:
            chat = '\n'.join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in server.members if channel.overwrites_for(member).send_messages == False and
                                    channel.overwrites_for(member).read_messages == None])
            if len(chat) > 0:
                html.extend("<p><strong>#{}</strong></p>\n<ul>{}</ul>\n".format(channel.name, chat))
            else:
                html.extend('<p><strong>#{}</strong></p>\n<p><span style="text-decoration: underline;">NONE</span></p>\n'.format(channel.name))



def member_has_muted_role(server):
    roles = ('Muted', 'Mute', 'muted', 'mute')
    for role in server.roles:
        if role.name in roles:
            members = '\n'.join(['<li>@' + member.name + '#' + member.discriminator + '</li>' for member in server.members if role in member.roles])
            if len(members) > 0:
                html.extend('<p><strong>Muted members in server:</strong> [{}]</p>\n<ol>\n{}\n</ol>'.format(role.name, members))
            else:
                html.extend('<p><strong>Muted members in server:</strong> [{}]</p>\n<blockquote>\n<p>NONE</p>\n</blockquote>'.format(role.name))


def _main(server):
    try:
        html_generate()
        _info(server)
        html.extend("<HR>\n")
        html.extend("""<h1 id='members'>== Members&nbsp;==</h1>
        """)
        _administrator(server)
        _ban(server)
        _kick(server)
        _manage_server(server)
        _manage_roles(server)
        _manage_channels(server)
        _manage_messages(server)
        html.extend("<HR/>\n")
        html.extend('<HR>\n')
        html.extend("""<h1 id= 'roles'>== Roles ==</h1>
        """)
        _check_roles_members(server)
        _check_roles_permissions(server)
        html.extend('<HR/>\n')
        html.extend('<HR>\n')
        html.extend("""<h1 id = 'channels'>== Channels ==</h1>
        """)
        _tc(server)
        role_check_channels_permissionsFalse(server)
        member_check_channels_permissionsFalse(server)
        _vm(server)
        html.extend('<HR/>\n')
        html.extend("""<p>&nbsp;</p>
<h3 style="text-align: center;"><a href="#top">Top</a></h3>
</BODY>
</HTML>""")

    except:
        print('\033[91m[-]Failed {}\033[0m'.format(server.id))
        pass

    s = file.format(server.id, datetime.datetime.now().strftime("%I.%M%p"))
    with open(s, "w", encoding='utf-8') as f: #ا
        for text in html:
            f.write(text)
    f.close()




bot.run(token)
