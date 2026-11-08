// Chance calibration for the replication check: uniform random 64-byte programs through cubff's own
// CheckSelfRep (via EvalParsedSelfrep). Usage: calib LANG N SEED THRESHOLD
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <string>
#include <vector>
#include <atomic>
#include "common.h"
static inline uint64_t sm64(uint64_t x){x+=0x9E3779B97F4A7C15ULL;x=(x^(x>>30))*0xBF58476D1CE4E5B9ULL;x=(x^(x>>27))*0x94D049BB133111EBULL;return x^(x>>31);}
int main(int argc,char**argv){
  std::string lang=argv[1]; long long N=atoll(argv[2]); uint64_t seed=strtoull(argv[3],0,10); size_t thr=atoi(argv[4]);
  LanguageInterface* L=const_cast<LanguageInterface*>(GetLanguage(lang));
  long long hits=0; size_t best=0; long long hist[65]={0};
  #pragma omp parallel for reduction(+:hits) schedule(dynamic,1024)
  for(long long i=0;i<N;i++){
    std::vector<uint8_t> p(64);
    for(int j=0;j<64;j+=8){uint64_t r=sm64(seed*0x100000000ULL+i*8+j/8);for(int k=0;k<8;k++)p[j+k]=(r>>(8*k))&255;}
    size_t sc=L->EvalParsedSelfrep(p,0,seed+i,false);
    if(sc>=thr){hits++;
      #pragma omp critical
      {printf("hit %lld score %zu ",i,sc);for(int j=0;j<64;j++)printf("%02x",p[j]);printf("\n");fflush(stdout);}
    }
    #pragma omp atomic
    hist[sc]++;
  }
  printf("N %lld hits %lld\nhist",N,hits);for(int s=0;s<=64;s++)if(hist[s])printf(" %d:%lld",s,hist[s]);printf("\n");
}
