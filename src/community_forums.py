# community_forums.py

class CommunityForums:
    def __init__(self):
        self.threads = {}
        self.moderated_posts = set()

    def add_comment(self, thread_id, comment_id, user, text):
        """Add a comment to a forum thread."""
        if thread_id not in self.threads:
            self.threads[thread_id] = []
        self.threads[thread_id].append({
            'comment_id': comment_id,
            'user': user,
            'text': text,
            'replies': []
        })
        return 'Comment added successfully.'

    def reply_to_comment(self, thread_id, parent_comment_id, reply_id, user, text):
        """Reply to a specific comment."""
        for comment in self.threads.get(thread_id, []):
            if comment['comment_id'] == parent_comment_id:
                comment['replies'].append({
                    'reply_id': reply_id,
                    'user': user,
                    'text': text
                })
                return 'Reply added successfully.'
        return 'Parent comment not found.'

    def moderate_post(self, thread_id, post_id):
        """Flag a post for moderation."""
        self.moderated_posts.add((thread_id, post_id))
        return 'Post flagged for moderation.'

# Example usage:
if __name__ == '__main__':
    forums = CommunityForums()
    print(forums.add_comment(thread_id=1, comment_id=101, user='UserA', text='How to make a healthy salad?'))
    print(forums.reply_to_comment(thread_id=1, parent_comment_id=101, reply_id=201, user='UserB', text='Try using kale and avocado!'))
    print(forums.moderate_post(thread_id=1, post_id=101))