// Crane-ladder sham A: identical to bff_noheads except that '.' and ',' (the two copy
// instructions) are no-ops. Every other byte value means what it means in bff_noheads.
#define BFF_CUSTOM_OPS
#include "bff.inc.h"

namespace {

const char *Bff::name() { return "bff_nocopy"; }

__device__ __host__ BffOp Bff::GetOpKind(char c) {
  switch (c) {
    case '[': return BffOp::kLoopStart;
    case ']': return BffOp::kLoopEnd;
    case '+': return BffOp::kPlus;
    case '-': return BffOp::kMinus;
    case '<': return BffOp::kDec0;
    case '>': return BffOp::kInc0;
    case '{': return BffOp::kDec1;
    case '}': return BffOp::kInc1;
    case 0: return BffOp::kNull;
    default: return BffOp::kNoop;
  }
}

}  // namespace
