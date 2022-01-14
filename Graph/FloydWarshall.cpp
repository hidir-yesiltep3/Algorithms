#include "the7.h"
using namespace std;
#define MAXN 100

const int INF = 1e7;
int dis[MAXN][MAXN];
int Next[MAXN][MAXN];



int min(int x, int y)
{
    return x < y ? x : y;
}


void initialise(int n, vector<vector<int> >& graph)
{
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            dis[i][j] = graph[i][j];
 
            // If there is no edge between two nodes, assign -1
            if (graph[i][j] == INF)
                Next[i][j] = -1;
            // In other cases, assign the time value of the road intersecting the nodes i and j.
            else
                Next[i][j] = j;
        }
    }
}


vector<int> constructPath(int u,
                        int v, vector<int> & path)
{
    // If there's no path between
    // node u and v, simply return
    // an empty array
    if (Next[u][v] == -1)
        return {};
 
    // Storing the path in a vector
    // vector<int> path = { u };
    while (u != v) {
        u = Next[u][v];
        path.push_back(u);
    }
    return path;
}

void floydWarshall(int V, vector<vector<int>> & graph)
{
    for (int k = 0; k < V; k++) {
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
 
                // We cannot travel through
                // edge that doesn't exist
                if (dis[i][k] == INF
                    || dis[k][j] == INF)
                    continue;
 
                if (dis[i][j] > dis[i][k]
                                    + dis[k][j]) {
                    dis[i][j] = dis[i][k]
                                + dis[k][j];
                    Next[i][j] = Next[i][k];
                }
            }
        }
    }
}




void FindRoute(int n, std::vector<Road> roads, int s, int d, int x, int y) {
  // You can change these variables. These are here for demo only.
  
  // Write your code here...
  vector<vector<int>> graph;
  
  for (int i = 0; i < n; i++)
  {
      vector<int> temp(n, INF);
      graph.push_back(temp);
  }
  
  int len = roads.size();
  for (int i = 0; i < len; i++)
  {
      int fst = roads[i].endpoints.first, snd = roads[i].endpoints.second;
      int tm = roads[i].time;
      graph[fst][snd] = tm;
      graph[snd][fst] = tm;
  }
  
  std::vector<int> path1 = {s};
  initialise(n, graph);
  floydWarshall(n, graph);
  constructPath(s, x, path1);
  constructPath(x, y, path1);
  constructPath(y, d, path1);
  
  std::vector<int> path2 = {s};
  constructPath(s, y, path2);
  constructPath(y, x, path2);
  constructPath(x, d, path2);
  
  int cost1 = 0, cost2 = 0;
  
  int len1 = path1.size();
  for (int i = 1; i < len1; i++)
  {
      cost1 += graph[path1[i]][path1[i-1]];
  }
  
  int len2 = path2.size();
  for (int i = 1; i < len2; i++)
  {
      cost2 += graph[path2[i]][path2[i-1]];
  }
  
  if (cost2 < cost1)
  {
    std::cout << cost2 << " ";
    PrintRange(path2.begin(), path2.end());
    std::cout << std::endl;
  }
  
  else
  {
      std::cout << cost1 << " ";
  PrintRange(path1.begin(), path1.end());
  std::cout << std::endl;
  }
  
  
  
  
  // Your output should be like this. You can change this as long as you keep
  // the output format. PrintRange function helps you print elements of
  // containers with iteratos (e.g., std::vector).
  
}
