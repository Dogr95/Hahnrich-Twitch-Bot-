const TwitchModule = require('twitch').default;
const ChatModule = require('twitch-chat-client').default;
require('dotenv').config();
const F = require('fs');
const CLIENT_ID = process.env.clientId;
const CLIENT_SECRET = process.env.clientSecret;
const channel_name = process.argv.slice(2).join();

(async () => {
    // const TwitchClient = TwitchModule.withCredentials(CLIENT_ID, accessToken);
    const tokenData = JSON.parse(await F.readFileSync('./tokens.json', function(err){if (err != null){console.log(err)}}));
    const TwitchClient = TwitchModule.withCredentials(CLIENT_ID, tokenData.accessToken, undefined, {
        clientSecret: CLIENT_SECRET,
        refreshToken: tokenData.refreshToken,
        expiry: tokenData.expiryTimestamp === null ? null : new Date(tokenData.expiryTimestamp),
        onRefresh: async ({ accessToken, refreshToken, expiryDate }) => {
            const newTokenData = {
                accessToken,
                refreshToken,
                expiryDate: expiryDate === null ? null : expiryDate.getTime()
            };
            await F.writeFileSync('./tokens.json', JSON.stringify(newTokenData, null, 4), function(err){if (err != null){console.log(err)}});
        }
    });
//     const chatClient = await ChatModule.forTwitchClient(TwitchClient, { channels: ['vertikarl'] });
//     await chatClient.connect();
//     chatClient.onPrivmsg((channel, user, message) => {
// 	if (message === '!ping') {
// 		chatClient.say(channel, 'Pong!');
// 	} else if (message === '!dice') {
// 		const diceRoll = Math.floor(Math.random() * 6) + 1;
// 		chatClient.say(channel, `@${user} rolled a ${diceRoll}`)
// 	}
// });
    const channel = await TwitchClient.helix.users.getUserByName(channel_name)
    const clip = await TwitchClient.helix.clips.createClip({ channelId: channel.id });
    const clip_send = "https://clips.twitch.tv/" + clip
    console.log(clip_send)
})();
