def friendship_timeline(friends_added, friends_removed):
    """
    Time: O(n + m), where n is the number of entries in friends_added and m is the number of entries in friends_removed.
    Space: O(n) for the active friendships dictionary.
    """

    friendships = []
    for removed in friends_removed:
        for added in friends_added:
            if sorted(removed['user_ids']) == sorted(added['user_ids']):
                friends_added.remove(added)
                friendships.append({
                    'user_ids': sorted(removed['user_ids']),
                    'start_date': added['created_at'],
                    'end_date': removed['created_at']
                })
                break
    return sorted(friendships, key=lambda x: x['user_ids'])

if __name__=='__main__':

    friends_added = [
        {'user_ids': [1, 2], 'created_at': '2020-01-01'},
        {'user_ids': [3, 2], 'created_at': '2020-01-02'},
        {'user_ids': [2, 1], 'created_at': '2020-02-02'},
        {'user_ids': [4, 1], 'created_at': '2020-02-02'}
    ]

    friends_removed = [
        {'user_ids': [2, 1], 'created_at': '2020-01-03'},
        {'user_ids': [2, 3], 'created_at': '2020-01-05'},
        {'user_ids': [1, 2], 'created_at': '2020-02-05'}
    ]

    # Expected output:
    #friendships = [{
    #    'user_ids': [1, 2],
    #    'start_date': '2020-01-01',
    #    'end_date': '2020-01-03'
    #   },
    #   {
    #    'user_ids': [1, 2],
    #    'start_date': '2020-02-02',
    #    'end_date': '2020-02-05'
    #   },
    #   {
    #    'user_ids': [2, 3],
    #    'start_date': '2020-01-02',
    #    'end_date': '2020-01-05'
    #   }]

    res = friendship_timeline(friends_added, friends_removed)
    print(res)