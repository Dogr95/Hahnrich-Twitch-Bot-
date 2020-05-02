require('dotenv').config();
const F = require('fs');
const TwitchModule = require('twitch').default;

const clientId = process.env.clientId;
const clientSecret = process.env.clientSecret;
const TwitchClient = TwitchModule.withClientCredentials(clientId, clientSecret);

const username = process.argv.slice(2).join();
async function clips(username) {
    const user = await TwitchClient.helix.users.getUserByName(username);
    const userid = user.id;
    let clips = "Clips for channel " + username + ":\n"
    for await (const clip of TwitchClient.helix.clips.getClipsForBroadcasterPaginated(userid)) {
			clips += clip['url'] + "\n";
		}
    clips += "This query was powered by: https://alleshusos.de"
    return clips

}
clips(username).then(Clips => F.writeFile("clips", Clips, function(err){if (err != null){console.log(err)}}))
