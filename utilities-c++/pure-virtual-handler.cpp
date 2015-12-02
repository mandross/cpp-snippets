#include <cassert>

extern "C"
{
static int __cxa_pure_virtual() __attribute__((noinline, used));
static int __cxa_pure_virtual()
{
    assert(0);
    return 0;
}
}
