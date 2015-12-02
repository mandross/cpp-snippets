namespace static_assert
{
    template <bool> struct STATIC_ASSERTION_FAILURE;
    template <> struct STATIC_ASSERTION_FAILURE<true> { enum { value = 1 }; };
    template <int> struct static_assert_test{};
}

#define JOIN(A, B)  DO_JOIN(A, B)
#define DO_JOIN(A, B)  A ## B

#define STATIC_ASSERT(...) \
    typedef static_assert::static_assert_test< \
        sizeof(static_assert::STATIC_ASSERTION_FAILURE<static_cast<bool>(__VA_ARGS__) >)> \
            JOIN(t_staticAssert, __LINE__)
