using UnityEngine;
using Photon.Pun;

public class NetworkManager : MonoBehaviourPunCallbacks
{
    void Start()
    {
        PhotonNetwork.ConnectUsingSettings();
    }

    public override void OnConnectedToMaster()
    {
        PhotonNetwork.JoinOrCreateRoom("CarRaceRoom", new Photon.Realtime.RoomOptions { MaxPlayers = 4 }, null);
    }

    public override void OnJoinedRoom()
    {
        Debug.Log("Connected to room!");
        // Instantiate car prefab for each player here, örnek:
        // PhotonNetwork.Instantiate("CarPrefab", spawnPosition, Quaternion.identity);
    }
}