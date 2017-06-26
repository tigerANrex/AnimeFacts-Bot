import discord

def get_list_of_unique_members(client):
    member_list = list(set(client.get_all_members()))
    return member_list

# returns iterable list containing Channel objects
def get_list_of_channels(client):
    channel_list = list(set(client.get_all_channels()))
    return channel_list

def get_list_of_online_members(client):
    member_list = get_list_of_unique_members(client)
    unique_member_list = []
    for m in member_list:
        if m.status != discord.Status.offline:
            unique_member_list.append(m)
    return unique_member_list
